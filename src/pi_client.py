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

    def __init__(self, rufus_client, debug=False):
        self.debug = debug
        self.rufus_client = rufus_client
        self._set_up_buttons()

    def _set_up_buttons(self):
        for activity_name, button in self.BUTTONS.items():
            # def shim_func():
            #     log.info(f'Pressed button {button} to perform activity: {activity_name.value}')
            #     if self.debug:
            #         log.warning(f'In debug mode, no HTTP requests, just logging, taking the poison pill ...')
            #         return
            #     self.rufus_client.request_activity(activity_name.value)
            # button.when_pressed = shim_func
            button.when_pressed = self.rufus_client.get_request_activity_method(activity_name, debug=self.debug)

    @classmethod
    def get_button(cls, activity_name):
        return cls.BUTTONS[activity_name]

    def run(self):
        pause()


# Do I really even need this?
if __name__ == '__main__':
    from .rufus_client import RufusClient
    rufus = RufusClient()
    client = PiClient(rufus)
    client.run()

