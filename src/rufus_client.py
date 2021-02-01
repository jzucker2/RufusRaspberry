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

    def get_url(self, activity_name, custom_value=None):
        base_url = self.base_url
        log.info(f'base_url: {base_url}')
        activity_url = Activities.get_activity_url_suffix(activity_name)
        log.info(f'activity_url: {activity_url}')
        if custom_value:
            activity_url = activity_url.format(value=custom_value)
            log.info(f'with custom_value: {activity_url}')
        final = parse.urljoin(base_url, activity_url)
        log.info(f'final: {final}')
        return final

    def request_activity(self, activity_name, custom_value=None):
        url = self.get_url(activity_name, custom_value=custom_value)
        log.info(url)
        log.info(f'Perform activity: {activity_name} with url => {url}')
        headers = {
            'user-agent': f'rufus-raspberry/{version}',
            'content-type': 'application/json',
        }
        activity_method = self.get_activity_method(activity_name)
        return requests.request(activity_method, url, headers=headers)

    def get_activity_method(self, activity_name):
        return Activities.get_activity_method(activity_name)

    def perform_perform_full_activity(self, activity_name, custom_value=None, debug=False, traffic_lights=None):
        if traffic_lights:
            traffic_lights.amber.on()
            traffic_lights.green.off()
            traffic_lights.red.off()
        log.info(f'Intending to perform activity: {activity_name.value}')
        if custom_value:
            log.info(f'... with custom_value: {custom_value}')
        if debug:
            log.warning(f'In debug mode, no HTTP requests, just logging, taking the poison pill ...')
            return
        response = self.request_activity(activity_name.value, custom_value=custom_value)
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
        traffic_lights.amber.off()
        traffic_lights.green.off()
        traffic_lights.red.off()
        return response

    def get_request_activity_button_func(self, activity_name, debug=False, traffic_lights=None):
        def dynamic_func():
            return self.perform_perform_full_activity(activity_name, debug=debug, traffic_lights=traffic_lights)
        return dynamic_func
