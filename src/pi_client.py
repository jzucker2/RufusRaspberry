import logging
from gpiozero import Button
from signal import pause
from .activities import Activities, ActivityName


log = logging.getLogger(__name__)


class PiClient(object):
    BUTTONS = {
        ActivityName.ALL_OFF: Button(Activities.get_activity_pin(ActivityName.ALL_OFF), bounce_time=0.5),
        ActivityName.APPLE_TV: Button(Activities.get_activity_pin(ActivityName.APPLE_TV), bounce_time=0.5),
        ActivityName.VINYL: Button(Activities.get_activity_pin(ActivityName.VINYL), bounce_time=0.5),
        ActivityName.BEDTIME: Button(Activities.get_activity_pin(ActivityName.BEDTIME), bounce_time=0.5),
    }

    def __init__(self, rufus_client):
        self.rufus_client = rufus_client
        for activity_name, button in self.BUTTONS.items():
            def shim_func():
                self.rufus_client.request_activity(activity_name)
            button.when_pressed = shim_func()

    @classmethod
    def get_button(cls, activity):
        return cls.BUTTONS[activity]

    def run(self):
        pause()

