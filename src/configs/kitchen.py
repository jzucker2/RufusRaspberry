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
        return ActivityName.KITCHEN_VOLUME_ADJUSTMENT

    @property
    def local_mute_activity_name(self):
        return ActivityName.KITCHEN_MUTE_TOGGLE

    @property
    def activities(self):
        return {
            ActivityName.ALL_OFF: Constants.BLUE_WIRE_PIN,
            ActivityName.VINYL: Constants.RED_WIRE_PIN,
            ActivityName.BEDTIME: Constants.YELLOW_WIRE_PIN,
        }
