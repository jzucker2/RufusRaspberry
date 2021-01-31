import logging
from enum import Enum
from .constants import Constants


log = logging.getLogger(__name__)


def get_log_level(debug=False):
    if debug:
        return logging.DEBUG
    return Constants.DEFAULT_LOG_LEVEL

class HTTPRequestMethod(Enum):
    GET = 'GET'
    PATCH = 'PATCH'

