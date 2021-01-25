from urllib import parse
import requests
import logging
from time import sleep
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

    def get_url(self, activity_name):
        base_url = self.base_url
        print(f'base_url: {base_url}')
        activity_url = Activities.get_activity_url_suffix(activity_name)
        print(f'activity_url: {activity_url}')
        final = parse.urljoin(base_url, activity_url)
        print(f'final: {final}')
        return final

    def request_activity(self, activity_name):
        url = self.get_url(activity_name)
        print(url)
        log.info(f'Perform activity: {activity_name} with url => {url}')
        headers = {
            'user-agent': f'rufus-raspberry/{version}',
            'content-type': 'application/json',
        }
        return requests.get(url, headers=headers)

    def get_request_activity_method(self, activity_name, debug=False, traffic_lights=None):
        def dynamic_func():
            if traffic_lights:
                traffic_lights.amber.on()
                traffic_lights.green.off()
                traffic_lights.red.off()
            log.info(f'Intending to perform activity: {activity_name.value}')
            if debug:
                log.warning(f'In debug mode, no HTTP requests, just logging, taking the poison pill ...')
                return
            response = self.request_activity(activity_name.value)
            if not traffic_lights:
                return response
            log.debug(f'Activating traffic lights')
            if response.status_code == 200:
                traffic_lights.amber.off()
                traffic_lights.green.on()
                traffic_lights.red.off()
            else:
                traffic_lights.amber.off()
                traffic_lights.green.off()
                traffic_lights.red.on()
            sleep(1)
            return response
        return dynamic_func
