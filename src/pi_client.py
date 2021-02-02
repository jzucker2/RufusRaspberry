import logging
from gpiozero import Button, TrafficLights
from signal import pause
from .constants import Constants
from .rotary_encoder import RotaryEncoderClickable
from .activities import ActivityName
from .simple_volume_adjuster import SimpleVolumeAdjuster, VolumeDomain


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
            self.volume_adjuster = SimpleVolumeAdjuster(self.rufus_client, self.config.local_volume_activity_name, self.config.local_mute_activity_name, debug=debug, traffic_lights=self.traffic_lights)
        if self.config.has_volume_domain_switch:
            log.info('set up volume domain switch!')
            self._set_up_volume_domain_switch()

    def _set_up_traffic_lights(self):
        self.traffic_lights = TrafficLights(*self.config.traffic_lights_pins)

    def _set_up_volume_domain_switch(self):
        self.volume_domain_switch = Button(*self.config.volume_domain_switch_pins)

    def _set_up_buttons(self):
        # for activity_name in list(ActivityName):
        for activity_name, pin in self.config.activities.items():
            button = Button(pin, bounce_time=Constants.DEFAULT_BOUNCE_TIME)
            button.when_pressed = self.rufus_client.get_request_activity_button_func(activity_name, debug=self.debug,
                                                                                     traffic_lights=self.traffic_lights)
            self.buttons[activity_name] = button

    def get_volume_domain_switch_state(self):
        if not self.config.has_volume_domain_switch:
            return None
        return self.volume_domain_switch.value

    def current_volume_domain(self):
        return VolumeDomain(self.get_volume_domain_switch_state())

    def rotary_encoder_rotated(self, value):
        # proposal! turning this will start a timer that collects clicks for 2 seconds, after 2 second, it fires off an async volume request
        # stopgap idea: only perform call if the dial hasn't spun for a full second? (Could lower by 2 as a compromise)
        # this is slowing things down!
        # look here! https://stackoverflow.com/questions/24687061/can-i-somehow-share-an-asynchronous-queue-with-a-subprocess
        log.warning(f'(value: {value}) current rotary encoder => {self.volume_rotary_encoder}')
        current_volume_domain = self.current_volume_domain()
        log.info(f'!!!!!!!! Current volume domain: {current_volume_domain}, now adjust volume ...')
        self.volume_adjuster.add_event(value, domain=current_volume_domain)

    def rotary_encoder_button_pressed(self):
        current_volume_domain = self.current_volume_domain()
        log.info(f'$$$$$$$$ Current volume domain: {current_volume_domain}, now toggling mute ...')
        self.volume_adjuster.toggle_mute(domain=current_volume_domain)

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
