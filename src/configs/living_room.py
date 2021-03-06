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
    def has_volume_rotary_encoder(self):
        return True

    @property
    def volume_rotary_encoder_pins(self):
        return list([
            Constants.ROTARY_RED_WIRE_PIN, Constants.ROTARY_YELLOW_WIRE_PIN, Constants.ROTARY_BLUE_WIRE_PIN
        ])

    @property
    def has_volume_domain_switch(self):
        return True

    @property
    def volume_domain_switch_pins(self):
        return list([
            Constants.GREEN_VOLUME_DOMAIN_WIRE_PIN
        ])

    @property
    def local_volume_activity_name(self):
        return ActivityName.LIVING_ROOM_VOLUME_ADJUSTMENT

    @property
    def local_mute_activity_name(self):
        return ActivityName.LIVING_ROOM_MUTE_TOGGLE

    @property
    def activities(self):
        return {
            ActivityName.ALL_OFF: Constants.BLUE_WIRE_PIN,
            ActivityName.APPLE_TV: Constants.GREEN_WIRE_PIN,
            ActivityName.VINYL: Constants.RED_WIRE_PIN,
            ActivityName.BEDTIME: Constants.YELLOW_WIRE_PIN,
            ActivityName.NIGHTLY_MOVIE: Constants.ORANGE_WIRE_PIN,
            ActivityName.WORK_FROM_HOME: Constants.BROWN_WIRE_PIN,
            ActivityName.YOGA: Constants.WHITE_WIRE_PIN,
        }
