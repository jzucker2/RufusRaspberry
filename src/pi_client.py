import logging
from gpiozero import Button, TrafficLights
from signal import pause
from .constants import Constants
from .rotary_encoder import RotaryEncoderClickable


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

    def _set_up_traffic_lights(self):
        self.traffic_lights = TrafficLights(*self.config.traffic_lights_pins)

    def _set_up_buttons(self):
        # for activity_name in list(ActivityName):
        for activity_name, pin in self.config.activities.items():
            button = Button(pin, bounce_time=Constants.DEFAULT_BOUNCE_TIME)
            button.when_pressed = self.rufus_client.get_request_activity_method(activity_name, debug=self.debug,
                                                                                traffic_lights=self.traffic_lights)
            self.buttons[activity_name] = button

    def _set_up_volume_rotary_encoder(self):
        log.info(f'using config values: {self.config.volume_rotary_encoder_pins}')
        if self.debug:
            log.debug('Skipping set up of rotary encoder during debug')
            return
        self.volume_rotary_encoder = RotaryEncoderClickable(*self.config.volume_rotary_encoder_pins)

    def turn_off_traffic_lights(self):
        if self.config.has_traffic_lights:
            self.traffic_lights.amber.off()
            self.traffic_lights.green.off()
            self.traffic_lights.red.off()

    def run(self):
        log.info('Start running ...')
        pause()
