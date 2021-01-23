import logging
from gpiozero import Button
from .activities import Activities, ActivityName


log = logging.getLogger(__name__)


class PiClient(object):
    def __init__(self, rufus_client):
        self.rufus_client = rufus_client

    BUTTONS = {
        ActivityName.ALL_OFF: Button(Activities.get_activity_pin(ActivityName.ALL_OFF), bounce_time=0.5),
        ActivityName.APPLE_TV: Button(Activities.get_activity_pin(ActivityName.APPLE_TV), bounce_time=0.5),
        ActivityName.VINYL: Button(Activities.get_activity_pin(ActivityName.VINYL), bounce_time=0.5),
        ActivityName.BEDTIME: Button(Activities.get_activity_pin(ActivityName.BEDTIME), bounce_time=0.5),
    }

    @classmethod
    def get_button(cls, activity):
        return cls.BUTTONS[activity]

    def run(self):
        while True:
            if self.get_button(ActivityName.ALL_OFF).is_pressed:
                print("all off pressed")
                response = self.rufus_client.request_activity(ActivityName.ALL_OFF)
                print(f'response => {response}')
            elif self.get_button(ActivityName.APPLE_TV).is_pressed:
                print("apple tv is pressed")
                response = self.rufus_client.request_activity(ActivityName.APPLE_TV)
                print(f'response => {response}')
            elif self.get_button(ActivityName.VINYL).is_pressed:
                print("vinyl is pressed")
                response = self.rufus_client.request_activity(ActivityName.VINYL)
                print(f'response => {response}')
            elif self.get_button(ActivityName.BEDTIME).is_pressed:
                print("bedtime is pressed")
                response = self.rufus_client.request_activity(ActivityName.BEDTIME)
                print(f'response => {response}')
            else:
                print("No button is pressed")
