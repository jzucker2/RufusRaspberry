import logging
from dataclasses import dataclass
from enum import Enum
from .constants import Constants


log = logging.getLogger(__name__)


@dataclass
class Activity:
    name: str
    url: str
    pin: int


class ActivityName(Enum):
    ALL_OFF = 'all-off'
    APPLE_TV = 'apple-tv'
    VINYL = 'vinyl'
    BEDTIME = 'bedtime'


class Activities(object):
    @classmethod
    def all_activity_names(cls):
        return cls.ACTIVITIES.keys()

    @classmethod
    def all_activities(cls):
        return cls.ACTIVITIES.values()

    @classmethod
    def get_activity_url_suffix(cls, activity_name):
        return cls.get_activity(activity_name).url

    @classmethod
    def get_activity_pin(cls, activity_name):
        return cls.get_activity(activity_name.value).pin

    @classmethod
    def get_activity(cls, activity_name):
        return cls.ACTIVITIES[activity_name]

    ACTIVITIES = {
        ActivityName.ALL_OFF.value: Activity(name=ActivityName.ALL_OFF.value, url='api/v1/activities/all-off?kitchen=0&dining_room=0', pin=Constants.BLUE_WIRE_PIN),
        ActivityName.APPLE_TV.value: Activity(name=ActivityName.APPLE_TV.value, url='api/v1/activities/apple-tv', pin=Constants.GREEN_WIRE_PIN),
        ActivityName.VINYL.value: Activity(name=ActivityName.VINYL.value, url='api/v1/activities/vinyl?kitchen=1&dining_room=1', pin=Constants.RED_WIRE_PIN),
        ActivityName.BEDTIME.value: Activity(name=ActivityName.BEDTIME.value, url='api/v1/activities/bedtime?kitchen=0&dining_room=0', pin=Constants.YELLOW_WIRE_PIN),
    }
