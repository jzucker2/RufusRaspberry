import logging
from dataclasses import dataclass
from enum import Enum
from .constants import Constants
from .utils import HTTPRequestMethod


log = logging.getLogger(__name__)


@dataclass
class Activity:
    name: str
    url: str
    pin: int
    method: str = HTTPRequestMethod.GET.value


class ActivityName(Enum):
    ALL_OFF = 'all-off'
    APPLE_TV = 'apple-tv'
    VINYL = 'vinyl'
    BEDTIME = 'bedtime'
    NIGHTLY_MOVIE = 'nightly-movie'
    WORK_FROM_HOME = 'work-from-home'
    YOGA = 'yoga'
    MASTER_VOLUME_UP = 'master-volume-up'
    MASTER_VOLUME_DOWN = 'master-volume-down'
    MASTER_TOGGLE_MUTE = 'master-toggle-mute'


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
    def get_activity_method(cls, activity_name):
        return cls.get_activity(activity_name.value).method

    @classmethod
    def get_activity(cls, activity_name):
        return cls.ACTIVITIES[activity_name]

    ACTIVITIES = {
        ActivityName.ALL_OFF.value: Activity(name=ActivityName.ALL_OFF.value, url='api/v1/activities/all-off?kitchen=0&dining_room=0', pin=Constants.BLUE_WIRE_PIN),
        ActivityName.APPLE_TV.value: Activity(name=ActivityName.APPLE_TV.value, url='api/v1/activities/apple-tv', pin=Constants.GREEN_WIRE_PIN),
        ActivityName.VINYL.value: Activity(name=ActivityName.VINYL.value, url='api/v1/activities/vinyl?kitchen=1&dining_room=1', pin=Constants.RED_WIRE_PIN),
        ActivityName.BEDTIME.value: Activity(name=ActivityName.BEDTIME.value, url='api/v1/activities/bedtime?kitchen=0&dining_room=0', pin=Constants.YELLOW_WIRE_PIN),
        ActivityName.NIGHTLY_MOVIE.value: Activity(name=ActivityName.NIGHTLY_MOVIE.value,
                                             url='api/v1/activities/nightly-movie',
                                             pin=Constants.ORANGE_WIRE_PIN),
        ActivityName.WORK_FROM_HOME.value: Activity(name=ActivityName.WORK_FROM_HOME.value,
                                                   url='api/v1/activities/wfh?kitchen=1&dining_room=1',
                                                   pin=Constants.BROWN_WIRE_PIN),
        ActivityName.YOGA.value: Activity(name=ActivityName.YOGA.value,
                                                    url='api/v1/activities/yoga?kitchen=0&dining_room=0',
                                                    pin=Constants.WHITE_WIRE_PIN),
        ActivityName.MASTER_VOLUME_UP.value: Activity(name=ActivityName.MASTER_VOLUME_UP.value,
                                                    url='api/v1/volume/step/1',
                                                    pin=Constants.ROTARY_RED_WIRE_PIN),
        ActivityName.MASTER_VOLUME_DOWN.value: Activity(name=ActivityName.MASTER_VOLUME_DOWN.value,
                                                    url='api/v1/volume/step/-1',
                                                    pin=Constants.ROTARY_BLUE_WIRE_PIN),
        ActivityName.MASTER_TOGGLE_MUTE.value: Activity(name=ActivityName.MASTER_TOGGLE_MUTE.value,
                                                        url='api/v1/volume/mute',
                                                        pin=Constants.ROTARY_YELLOW_WIRE_PIN, method=HTTPRequestMethod.PATCH.value),
    }
