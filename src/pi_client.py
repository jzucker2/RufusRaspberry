import logging
import asyncio
import functools
from gpiozero import Button, TrafficLights
from signal import pause
from .constants import Constants
from .rotary_encoder import RotaryEncoderClickable
from .activities import ActivityName


log = logging.getLogger(__name__)


class PiClient(object):
    def __init__(self, rufus_client, config, debug=False):
        self.debug = debug
        self.rufus_client = rufus_client
        self.config = config
        # set up leds first because we pass them to buttons
        self.traffic_lights = None
        if self.config.has_traffic_lights:
            self._set_up_traffic_lights()
        self.buttons = {}
        self._set_up_buttons()
        if self.config.has_volume_rotary_encoder:
            log.info('set up volume rotary encoder!')
            self._set_up_volume_rotary_encoder()
        # self.pool = Pool(10) # Creates a pool with ten threads; more threads = more concurrency.
        #         # "pool" is a module attribute; you can be sure there will only
        #         # be one of them in your application
        #         # as modules are cached after initialization.
        # self.futures = []
        self.loop = asyncio.get_event_loop()
        asyncio.set_event_loop(self.loop)

    def _set_up_traffic_lights(self):
        self.traffic_lights = TrafficLights(*self.config.traffic_lights_pins)

    def _set_up_buttons(self):
        # for activity_name in list(ActivityName):
        for activity_name, pin in self.config.activities.items():
            button = Button(pin, bounce_time=Constants.DEFAULT_BOUNCE_TIME)
            button.when_pressed = self.rufus_client.get_request_activity_button_func(activity_name, debug=self.debug,
                                                                                     traffic_lights=self.traffic_lights)
            self.buttons[activity_name] = button

    def rotary_encoder_rotated(self, value):
        log.warning(f'(value: {value}) current rotary encoder => {self.volume_rotary_encoder}')
        activity_name = None
        if value > 0:
            log.info("clockwise ... volume up!")
            activity_name = ActivityName.MASTER_VOLUME_UP
        else:
            log.info("counterclockwise ... volume down!")
            activity_name = ActivityName.MASTER_VOLUME_DOWN
        # traffic lights must be None because the `sleep()` throws off the rotary encoder
        # future = self.pool.apply_async(self.rufus_client.perform_perform_full_activity, args=(activity_name), kwds={'debug':self.debug, 'traffic_lights': None})
        # self.futures.append(future)
        # https://docs.python.org/3.7/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe
        # # will schedule "print("Hello", flush=True)"
        # loop.call_soon(
        #     functools.partial(print, "Hello", flush=True))
        callable = functools.partial(self.rufus_client.perform_perform_full_activity, activity_name, debug=self.debug, traffic_lights=None)
        self.loop.call_soon_threadsafe(callable)

    def rotary_encoder_button_pressed(self):
        log.info('rotary encoder button pressed ... muting')
        self.rufus_client.perform_perform_full_activity(ActivityName.MASTER_TOGGLE_MUTE, debug=self.debug,
                                                        traffic_lights=self.traffic_lights)

    def _set_up_volume_rotary_encoder(self):
        log.info(f'using config values: {self.config.volume_rotary_encoder_pins}')
        if self.debug:
            log.debug('Skipping set up of rotary encoder during debug')
            return
        self.volume_rotary_encoder = RotaryEncoderClickable(*self.config.volume_rotary_encoder_pins)
        self.volume_rotary_encoder.when_rotated = self.rotary_encoder_rotated
        self.volume_rotary_encoder.when_pressed = self.rotary_encoder_button_pressed

    def turn_off_traffic_lights(self):
        if self.config.has_traffic_lights:
            self.traffic_lights.amber.off()
            self.traffic_lights.green.off()
            self.traffic_lights.red.off()

    def run(self):
        log.info('Start running ...')
        pause()
