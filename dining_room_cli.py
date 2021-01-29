#!/usr/bin/env python3

import logging
from src.rufus_client import RufusClient
from src.pi_client import PiClient
from src.arg_parser import create_argparser
from src.utils import get_log_level
from src.configs.living_room import LivingRoomConfig


log = logging.getLogger(__name__)


def main():
    arg_parser = create_argparser()
    args = arg_parser.parse_args()
    log_level = get_log_level(args.debug)
    logging.basicConfig(level=log_level)
    log.info(f'Set log_level to {log_level}')
    rufus_client = RufusClient(ip=args.ip)
    living_room_config = LivingRoomConfig()
    pi_client = PiClient(rufus_client, living_room_config, debug=args.debug)
    pi_client.run()

if __name__ == '__main__':
    main()
