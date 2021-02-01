import logging
from functools import reduce
from dataclasses import dataclass
from enum import Enum
from datetime import datetime, timedelta
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


@dataclass
class RotationEvent:
    value: int
    created: datetime

    @classmethod
    def create_event(cls, value):
        return cls(value, datetime.utcnow())
    
    @property
    def direction(self) -> RotationDirection:
        if self.value > 0:
            return RotationDirection.CLOCKWISE
        return RotationDirection.COUNTER_CLOCKWISE

    @property
    def activity_name(self) -> ActivityName:
        return self.direction.activity_name


class AbstractVolumeAdjuster(object):
    def __init__(self, rufus_client, traffic_lights=None, debug=False):
        self.events = []
        self.rufus_client = rufus_client
        self.traffic_lights = traffic_lights
        self.debug = debug

    def clear_events(self):
        self.events = []

    def add_event(self, value) -> RotationEvent:
        event = RotationEvent.create_event(value)
        self.events.append(event)
        return event

    def adjust_volume(self, value):
        activity_name = ActivityName.MASTER_VOLUME_ADJUSTMENT
        response = self.rufus_client.perform_perform_full_activity(activity_name, custom_value=value, debug=self.debug, traffic_lights=self.traffic_lights)
        log.info(f'For volume adjustment, got: {response}')
        return response


class SimpleVolumeAdjuster(AbstractVolumeAdjuster):

    @property
    def request_delay(self):
        return 1

    def add_event(self, value):
        event = super(SimpleVolumeAdjuster, self).add_event(value)
        now = datetime.utcnow()
        if now - event.created < timedelta(seconds=self.request_delay):
            log.info(f'less than 2 seconds')
            total_volume = self.get_total_adjustment()
            log.info(f'Got total_volume: {total_volume}')
            if total_volume == 0:
                self.clear_events()
                return
            self.adjust_volume(value)
            self.clear_events()

    def get_total_adjustment(self):
        return reduce(lambda x, y:x.value+y, self.events)
