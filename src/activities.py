import logging
from dataclasses import dataclass
from enum import Enum
from .utils import HTTPRequestMethod


log = logging.getLogger(__name__)


@dataclass
class Activity:
    name: str
    url: str
    method: str = HTTPRequestMethod.GET.value


class ActivityName(Enum):
    ALL_OFF = 'all-off'
    APPLE_TV = 'apple-tv'
    VINYL = 'vinyl'
    BEDTIME = 'bedtime'
    LEAVE_ALBION = 'leave-albion'
    WELCOME_HOME = 'welcome-home'
    NIGHTLY_MOVIE = 'nightly-movie'
    WORK_FROM_HOME = 'work-from-home'
    YOGA = 'yoga'
    MASTER_VOLUME_UP = 'master-volume-up'
    MASTER_VOLUME_DOWN = 'master-volume-down'
    MASTER_TOGGLE_MUTE = 'master-toggle-mute'
    LIVING_ROOM_VOLUME_ADJUSTMENT = 'living-room-volume-adjustment'
    DINING_ROOM_VOLUME_ADJUSTMENT = 'dining-room-volume-adjustment'
    KITCHEN_VOLUME_ADJUSTMENT = 'kitchen-volume-adjustment'
    GLOBAL_VOLUME_ADJUSTMENT = 'global-volume-adjustment'
    LIVING_ROOM_MUTE_TOGGLE = 'living-room-mute-toggle'
    DINING_ROOM_MUTE_TOGGLE = 'dining-room-mute-toggle'
    KITCHEN_MUTE_TOGGLE = 'kitchen-mute-toggle'
    GLOBAL_MUTE_TOGGLE = 'global-mute-toggle'



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
    def get_activity_method(cls, activity_name_string):
        return cls.get_activity(activity_name_string).method

    @classmethod
    def get_activity(cls, activity_name):
        return cls.ACTIVITIES[activity_name]

    ACTIVITIES = {
        ActivityName.ALL_OFF.value: Activity(name=ActivityName.ALL_OFF.value, url='api/v1/activities/all-off?kitchen=0&dining_room=0'),
        ActivityName.APPLE_TV.value: Activity(name=ActivityName.APPLE_TV.value, url='api/v1/activities/apple-tv'),
        ActivityName.VINYL.value: Activity(name=ActivityName.VINYL.value, url='api/v1/activities/vinyl?kitchen=1&dining_room=1'),
        ActivityName.BEDTIME.value: Activity(name=ActivityName.BEDTIME.value, url='api/v1/activities/bedtime?kitchen=0&dining_room=0'),
        ActivityName.LEAVE_ALBION.value: Activity(name=ActivityName.LEAVE_ALBION.value,
                                             url='api/v1/activities/leave?kitchen=0&dining_room=0'),
        ActivityName.WELCOME_HOME.value: Activity(name=ActivityName.WELCOME_HOME.value,
                                             url='api/v1/activities/welcome-home'),
        ActivityName.NIGHTLY_MOVIE.value: Activity(name=ActivityName.NIGHTLY_MOVIE.value,
                                             url='api/v1/activities/nightly-movie'),
        ActivityName.WORK_FROM_HOME.value: Activity(name=ActivityName.WORK_FROM_HOME.value,
                                                   url='api/v1/activities/wfh?kitchen=1&dining_room=1'),
        ActivityName.YOGA.value: Activity(name=ActivityName.YOGA.value,
                                                    url='api/v1/activities/yoga?kitchen=0&dining_room=0'),
        ActivityName.MASTER_VOLUME_UP.value: Activity(name=ActivityName.MASTER_VOLUME_UP.value,
                                                    url='api/v1/volume/step/1'),
        ActivityName.MASTER_VOLUME_DOWN.value: Activity(name=ActivityName.MASTER_VOLUME_DOWN.value,
                                                    url='api/v1/volume/step/-1'),
        ActivityName.LIVING_ROOM_VOLUME_ADJUSTMENT.value: Activity(name=ActivityName.LIVING_ROOM_VOLUME_ADJUSTMENT.value,
                                                                   url='api/v1/volume/step/{value}'),
        ActivityName.KITCHEN_VOLUME_ADJUSTMENT.value: Activity(
            name=ActivityName.KITCHEN_VOLUME_ADJUSTMENT.value,
            url='api/v1/volume/zone_name/kitchen/step/{value}'),
        ActivityName.DINING_ROOM_VOLUME_ADJUSTMENT.value: Activity(
            name=ActivityName.DINING_ROOM_VOLUME_ADJUSTMENT.value,
            url='api/v1/volume/zone_name/dining_room/step/{value}'),
        ActivityName.GLOBAL_VOLUME_ADJUSTMENT.value: Activity(
            name=ActivityName.GLOBAL_VOLUME_ADJUSTMENT.value,
            url='api/v1/volume/global/step/{value}'),
        ActivityName.MASTER_TOGGLE_MUTE.value: Activity(name=ActivityName.MASTER_TOGGLE_MUTE.value,
                                                        url='api/v1/volume/mute',
                                                        method=HTTPRequestMethod.PATCH.value),
        ActivityName.LIVING_ROOM_MUTE_TOGGLE.value: Activity(
            name=ActivityName.LIVING_ROOM_MUTE_TOGGLE.value,
            url='api/v1/volume/mute', # works for just main zone
            method=HTTPRequestMethod.PATCH.value),
        ActivityName.KITCHEN_MUTE_TOGGLE.value: Activity(
            name=ActivityName.KITCHEN_MUTE_TOGGLE.value,
            url='api/v1/volume/zone_name/kitchen/toggle-mute',
            method=HTTPRequestMethod.PATCH.value),
        ActivityName.DINING_ROOM_MUTE_TOGGLE.value: Activity(
            name=ActivityName.DINING_ROOM_MUTE_TOGGLE.value,
            url='api/v1/volume/zone_name/dining_room/toggle-mute',
            method=HTTPRequestMethod.PATCH.value),
        ActivityName.GLOBAL_MUTE_TOGGLE.value: Activity(
            name=ActivityName.GLOBAL_MUTE_TOGGLE.value,
            url='api/v1/volume/global/toggle-mute',
            method=HTTPRequestMethod.PATCH.value),
    }
