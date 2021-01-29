#!/usr/bin/env python3

import logging
from src.remote_process import process
from src.configs.kitchen import KitchenConfig


log = logging.getLogger(__name__)


def main():
    log.info('Starting kitchen ...')
    process(KitchenConfig)

if __name__ == '__main__':
    main()
