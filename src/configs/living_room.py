from ..controller_config import ControllerConfig
from ..activities import ActivityName
from ..constants import Constants

class LivingRoomConfig(ControllerConfig):

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
            ActivityName.ALL_OFF: Constants.BLUE_WIRE_PIN,
            ActivityName.APPLE_TV: Constants.GREEN_WIRE_PIN,
            ActivityName.VINYL: Constants.RED_WIRE_PIN,
            ActivityName.BEDTIME: Constants.YELLOW_WIRE_PIN,
            ActivityName.NIGHTLY_MOVIE: Constants.ORANGE_WIRE_PIN,
            ActivityName.WORK_FROM_HOME: Constants.BROWN_WIRE_PIN,
            ActivityName.YOGA.value: Constants.WHITE_WIRE_PIN,
        }
