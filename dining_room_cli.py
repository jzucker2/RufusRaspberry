#!/usr/bin/env python3

import logging
from src.remote_process import run_remote
from src.configs.dining_room import DiningRoomConfig


log = logging.getLogger(__name__)


def main():
    log.info('Starting dining room ...')
    run_remote(DiningRoomConfig)

if __name__ == '__main__':
    main()
