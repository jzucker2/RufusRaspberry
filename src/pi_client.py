import logging
from gpiozero import Button, TrafficLights
from signal import pause
from .activities import Activities, ActivityName
from .constants import Constants


log = logging.getLogger(__name__)


class PiClient(object):
    def __init__(self, rufus_client, debug=False):
        self.debug = debug
        self.rufus_client = rufus_client
        # set up leds first because we pass them to buttons
        self._set_up_traffic_lights()
        self.buttons = {}
        self._set_up_buttons()

    def _set_up_traffic_lights(self):
        self.traffic_lights = TrafficLights(Constants.RED_LED_PIN, Constants.AMBER_LED_PIN, Constants.GREEN_LED_PIN)

    def _set_up_buttons(self):
        for activity_name in list(ActivityName):
            button = Button(Activities.get_activity_pin(activity_name), bounce_time=Constants.DEFAULT_BOUNCE_TIME)
            button.when_pressed = self.rufus_client.get_request_activity_method(activity_name, debug=self.debug,
                                                                                traffic_lights=self.traffic_lights)
            self.buttons[activity_name] = button

    def run(self):
        log.info('Start running ...')
        pause()


# Do I really even need this?
if __name__ == '__main__':
    from .rufus_client import RufusClient
    rufus = RufusClient()
    client = PiClient(rufus)
    client.run()

