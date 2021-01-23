from urllib import parse
from dataclasses import dataclass
import requests
import logging
from .version import version


log = logging.getLogger(__name__)


@dataclass
class Activity:
    name: str
    url: str


class RufusClient(object):
    def __init__(self, ip):
        log.info(f'Setting ip to {ip}')
        self.ip = ip

    @property
    def base_url(self):
        return self.ip

    def get_activity(self, activity):
        return self.ACTIVITIES[activity]

    def get_activity_url_suffix(self, activity):
        return self.get_activity(activity).url

    def get_url(self, activity):
        base_url = self.base_url
        print(f'base_url: {base_url}')
        activity_url = self.get_activity_url_suffix(activity)
        print(f'activity_url: {activity_url}')
        final = parse.urljoin(base_url, activity_url)
        print(f'final: {final}')
        return final

    @classmethod
    def all_activites(cls):
        return cls.ACTIVITIES.keys()

    ACTIVITIES = {
        'all-off': Activity(name='all-off', url='api/v1/activities/all-off?kitchen=0&dining_room=0'),
        'apple-tv': Activity(name='apple-tv', url='api/v1/activities/apple-tv'),
        'vinyl': Activity(name='vinyl', url='api/v1/activities/vinyl?kitchen=1&dining_room=1'),
        'bedtime': Activity(name='bedtime', url='api/v1/activities/bedtime?kitchen=0&dining_room=0'),
    }

    def request_activity(self, activity):
        url = self.get_url(activity)
        print(url)
        log.info(f'Perform activity: {activity} with url => {url}')
        headers = {
            'user-agent': f'rufus-raspberry/{version}',
            'content-type': 'application/json',
        }
        return requests.get(url, headers=headers)
