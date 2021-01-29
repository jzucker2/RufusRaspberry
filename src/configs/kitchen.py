from ..controller_config import ControllerConfig
from ..activities import ActivityName
from ..constants import Constants

class KitchenConfig(ControllerConfig):

    @property
    def has_traffic_lights(self):
        return True

    @property
    def traffic_lights_pins(self):
        return list([
            Constants.RED_LED_PIN, Constants.AMBER_LED_PIN, Constants.GREEN_LED_PIN
        ])

    @property
    def activities(self):
        return {
            ActivityName.ALL_OFF.value: Constants.BLUE_WIRE_PIN,
            ActivityName.VINYL.value: Constants.RED_WIRE_PIN,
            ActivityName.BEDTIME.value: Constants.YELLOW_WIRE_PIN,
        }
