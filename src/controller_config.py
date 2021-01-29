import logging
from .activities import Activities, ActivityName
from .constants import Constants


log = logging.getLogger(__name__)


class ControllerConfigException(Exception): pass
class TrafficLightsPinsUnassignedException(ControllerConfigException): pass


class ControllerConfig(object):
    def __init__(self, debug=False):
        self.debug = debug
        # set up leds first because we pass them to buttons
        # self._set_up_traffic_lights()
        # self.buttons = {}
        # self._set_up_buttons()

    @property
    def has_traffic_lights(self):
        return False

    @property
    def traffic_lights_pins(self):
        raise TrafficLightsPinsUnassignedException('No pins assigned!')

    @property
    def activities(self):
        return {}

    # def _set_up_traffic_lights(self):
    #     self.traffic_lights = TrafficLights(Constants.RED_LED_PIN, Constants.AMBER_LED_PIN, Constants.GREEN_LED_PIN)
    #
    # def _set_up_buttons(self):
    #     for activity_name in list(ActivityName):
    #         button = Button(Activities.get_activity_pin(activity_name), bounce_time=Constants.DEFAULT_BOUNCE_TIME)
    #         button.when_pressed = self.rufus_client.get_request_activity_method(activity_name, debug=self.debug,
    #                                                                             traffic_lights=self.traffic_lights)
    #         self.buttons[activity_name] = button
    #
    # def turn_off_traffic_lights(self):
    #     self.traffic_lights.amber.off()
    #     self.traffic_lights.green.off()
    #     self.traffic_lights.red.off()
    #
    # def run(self):
    #     log.info('Start running ...')
    #     pause()


# # Do I really even need this?
# if __name__ == '__main__':
#     from .rufus_client import RufusClient
#     rufus = RufusClient()
#     client = PiClient(rufus)
#     client.run()