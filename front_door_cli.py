#!/usr/bin/env python3

import logging
from src.remote_process import process
from src.configs.front_door import FrontDoorConfig


log = logging.getLogger(__name__)


def main():
    log.info('Starting front door ...')
    process(FrontDoorConfig)

if __name__ == '__main__':
    main()
