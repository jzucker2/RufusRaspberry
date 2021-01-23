from urllib import parse
import requests
import logging
from .version import version
from .constants import Constants
from .activities import Activities


log = logging.getLogger(__name__)


class RufusClient(object):
    def __init__(self, ip=Constants.DEFAULT_IP):
        log.info(f'Setting ip to {ip}')
        self.ip = ip

    @property
    def base_url(self):
        return self.ip

    def get_url(self, activity):
        base_url = self.base_url
        print(f'base_url: {base_url}')
        activity_url = Activities.get_activity_url_suffix(activity)
        print(f'activity_url: {activity_url}')
        final = parse.urljoin(base_url, activity_url)
        print(f'final: {final}')
        return final

    def request_activity(self, activity):
        url = self.get_url(activity)
        print(url)
        log.info(f'Perform activity: {activity} with url => {url}')
        headers = {
            'user-agent': f'rufus-raspberry/{version}',
            'content-type': 'application/json',
        }
        return requests.get(url, headers=headers)
