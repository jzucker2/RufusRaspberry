import logging


log = logging.getLogger(__name__)


class Constants(object):
    DEFAULT_IP = 'http://10.0.1.104:5000'

    BLUE_WIRE_PIN = 2
    GREEN_WIRE_PIN = 4
    RED_WIRE_PIN = 17
    YELLOW_WIRE_PIN = 22
    ORANGE_WIRE_PIN = 10
    BROWN_WIRE_PIN = 11
    WHITE_WIRE_PIN = 5

    # LEDs
    RED_LED_PIN = 14
    AMBER_LED_PIN = 15
    GREEN_LED_PIN = 18

    # Rotary Encoder
    ROTARY_RED_WIRE_PIN = 6
    ROTARY_YELLOW_WIRE_PIN = 13
    ROTARY_BLUE_WIRE_PIN = 19

    DEFAULT_LOG_LEVEL = logging.INFO

    # turns out this needs to be `None`?
    # https://github.com/gpiozero/gpiozero/issues/550
    DEFAULT_BOUNCE_TIME = None
