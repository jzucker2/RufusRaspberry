import logging


log = logging.getLogger(__name__)


class Constants(object):
    DEFAULT_IP = 'http://10.0.1.104:5000'

    BLUE_WIRE_PIN = 2
    GREEN_WIRE_PIN = 4
    RED_WIRE_PIN = 17
    YELLOW_WIRE_PIN = 22

    DEFAULT_LOG_LEVEL = logging.INFO

    # turns out this needs to be `None`?
    # https://github.com/gpiozero/gpiozero/issues/550
    DEFAULT_BOUNCE_TIME = None
