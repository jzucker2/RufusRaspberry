#!/usr/bin/env python3

import logging
from src.remote_process import process
from src.configs.dining_room import DiningRoomConfig


log = logging.getLogger(__name__)


def main():
    log.info('Starting dining room ...')
    process(DiningRoomConfig)

if __name__ == '__main__':
    main()
