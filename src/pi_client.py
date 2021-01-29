import logging
from gpiozero import Button, TrafficLights
from signal import pause
from .activities import Activities, ActivityName
from .constants import Constants


log = logging.getLogger(__name__)


class PiClient(object):
    def __init__(self, rufus_client, config, debug=False):
        self.debug = debug
        self.rufus_client = rufus_client
        self.config = config
        # set up leds first because we pass them to buttons
        self.traffic_lights = None
        if self.config.has_traffic_lights():
            self._set_up_traffic_lights()
        self.buttons = {}
        self._set_up_buttons()

    def _set_up_traffic_lights(self):
        self.traffic_lights = TrafficLights(*self.config.traffic_lights_pins)

    def _set_up_buttons(self):
        # for activity_name in list(ActivityName):
        for activity_name, pin in self.config.activities:
            button = Button(pin, bounce_time=Constants.DEFAULT_BOUNCE_TIME)
            button.when_pressed = self.rufus_client.get_request_activity_method(activity_name, debug=self.debug,
                                                                                traffic_lights=self.traffic_lights)
            self.buttons[activity_name] = button

    def turn_off_traffic_lights(self):
        if self.traffic_lights:
            self.traffic_lights.amber.off()
            self.traffic_lights.green.off()
            self.traffic_lights.red.off()

    def run(self):
        log.info('Start running ...')
        pause()


# # Do I really even need this?
# if __name__ == '__main__':
#     from .rufus_client import RufusClient
#     rufus = RufusClient()
#     client = PiClient(rufus)
#     client.run()

