import logging
from .activities import Activities, ActivityName
from .constants import Constants


log = logging.getLogger(__name__)


class ControllerConfigException(Exception): pass
class TrafficLightsPinsUnassignedException(ControllerConfigException): pass
class VolumeRotaryEncoderPinsUnassignedException(ControllerConfigException): pass


class ControllerConfig(object):
    def __init__(self, debug=False):
        self.debug = debug

    @property
    def has_traffic_lights(self):
        return False

    @property
    def traffic_lights_pins(self):
        raise TrafficLightsPinsUnassignedException('No pins assigned!')

    @property
    def activities(self):
        return {}

    @property
    def has_volume_rotary_encoder(self):
        return False

    @property
    def volume_rotary_encoder_pins(self):
        raise VolumeRotaryEncoderPinsUnassignedException('No pins assigned!')
