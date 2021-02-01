import logging
from functools import reduce
from dataclasses import dataclass
from enum import Enum
from datetime import datetime, timedelta
import threading
from .activities import ActivityName


log = logging.getLogger(__name__)


class RotationDirectionException(Exception): pass


class RotationDirection(Enum):
    CLOCKWISE = 1
    COUNTER_CLOCKWISE = -1

    @property
    def activity_name(self):
        if self == self.CLOCKWISE:
            return ActivityName.MASTER_VOLUME_UP
        elif self == self.COUNTER_CLOCKWISE:
            return ActivityName.MASTER_VOLUME_DOWN
        else:
            raise RotationDirectionException(f'Unexpected direction: {self}')

class VolumeDomain(Enum):
    GLOBAL = 1
    LOCAL = 0

    def __repr__(self):
        return f'VolumeDomain => {self.name} ({self.value})'


@dataclass
class RotationEvent:
    value: int
    created: datetime
    domain: VolumeDomain = VolumeDomain.LOCAL

    @classmethod
    def create_event(cls, value, domain=VolumeDomain.LOCAL):
        return cls(value, datetime.utcnow(), domain=domain)
    
    @property
    def direction(self) -> RotationDirection:
        if self.value > 0:
            return RotationDirection.CLOCKWISE
        return RotationDirection.COUNTER_CLOCKWISE

    @property
    def activity_name(self) -> ActivityName:
        return self.direction.activity_name

    def __int__(self):
        return self.value


class AbstractVolumerAdjusterException(Exception): pass
class NoEventsAbstractVolumeAdjusterException(AbstractVolumerAdjusterException): pass


class AbstractVolumeAdjuster(object):
    def __init__(self, rufus_client, local_activity_name, traffic_lights=None, debug=False):
        self.events = []
        self.rufus_client = rufus_client
        self.traffic_lights = traffic_lights
        self.debug = debug
        self.local_activity_name = local_activity_name

    def clear_events(self):
        self.events = []

    def add_event(self, value, domain=None) -> RotationEvent:
        event = RotationEvent.create_event(value, domain=domain)
        self.events.append(event)
        return event

    def get_activity_for_domain(self, domain):
        if domain == VolumeDomain.GLOBAL:
            return ActivityName.GLOBAL_VOLUME_ADJUSTMENT
        return self.local_activity_name

    def adjust_volume(self, value, domain=VolumeDomain.LOCAL):
        activity_name = self.get_activity_for_domain(domain)
        log.info(f'About to adjust volume ({value}) for domain: {domain}')
        response = self.rufus_client.perform_perform_full_activity(activity_name, custom_value=value, debug=self.debug, traffic_lights=self.traffic_lights)
        log.info(f'For volume adjustment, got: {response}')
        return response

    def last_event_datetime(self):
        if len(self.events):
            event = self.events[-1]
            return event.created
        raise NoEventsAbstractVolumeAdjusterException('No events!')

    def last_event_info(self):
        if len(self.events):
            event = self.events[-1]
            return {
                'created': event.created,
                'domain': event.domain,
            }
        raise NoEventsAbstractVolumeAdjusterException('No events!')


class SimpleVolumeAdjuster(AbstractVolumeAdjuster):

    def __init__(self, rufus_client, local_activity_name, traffic_lights=None, debug=False):
        super(SimpleVolumeAdjuster, self).__init__(rufus_client, local_activity_name, traffic_lights=traffic_lights, debug=debug)
        self.timer = None

    @property
    def request_delay(self):
        return 1

    @property
    def event_debounce_duration(self):
        return 1

    def add_event(self, value, domain=None):
        super(SimpleVolumeAdjuster, self).add_event(value, domain=domain)
        if self.timer:
            self.timer.cancel()
        self.timer = threading.Timer(self.request_delay, self.simple_volume_request)
        self.timer.start()

    def simple_volume_request(self):
        now = datetime.utcnow()
        last_event_info = self.last_event_info()
        time_difference = now - last_event_info['created']
        if time_difference < timedelta(seconds=self.event_debounce_duration):
            log.info(f'Only been {time_difference} so no request yet, returning ...')
            return
        domain = last_event_info['domain']
        total_volume = self.get_total_adjustment()
        log.info(f'Got total_volume: {total_volume} for intended domain: {domain}')
        self.clear_events()
        if total_volume == 0:
            return
        self.adjust_volume(total_volume, domain=domain)

    def get_total_adjustment(self):
        return reduce(lambda x, y:int(x)+int(y), self.events)
