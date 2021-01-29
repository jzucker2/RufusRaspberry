#!/usr/bin/env python3

import logging
from src.remote_process import process
from src.configs.living_room import LivingRoomConfig


log = logging.getLogger(__name__)


def main():
    log.info('Starting living room ...')
    process(LivingRoomConfig)

if __name__ == '__main__':
    main()
