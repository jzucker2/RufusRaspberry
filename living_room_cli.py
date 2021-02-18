#!/usr/bin/env python3

import logging
from src.remote_process import run_remote
from src.configs.living_room import LivingRoomConfig


log = logging.getLogger(__name__)


def main():
    log.info('Starting living room ...')
    run_remote(LivingRoomConfig)

if __name__ == '__main__':
    main()
