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
            ActivityName.ALL_OFF.value: Constants.BLUE_WIRE_PIN,
            ActivityName.APPLE_TV.value: Constants.GREEN_WIRE_PIN,
            ActivityName.VINYL.value: Constants.RED_WIRE_PIN,
            ActivityName.BEDTIME.value: Constants.YELLOW_WIRE_PIN,
            ActivityName.NIGHTLY_MOVIE.value: Constants.ORANGE_WIRE_PIN,
            ActivityName.WORK_FROM_HOME.value: Constants.BROWN_WIRE_PIN,
        }
