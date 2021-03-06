#!/usr/bin/env python3

import logging
from src.remote_process import run_remote
from src.configs.front_door import FrontDoorConfig


log = logging.getLogger(__name__)


def main():
    log.info('Starting front door ...')
    run_remote(FrontDoorConfig)

if __name__ == '__main__':
    main()
