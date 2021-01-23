#!/usr/bin/env python3

import logging
from src.rufus_client import RufusClient
from src.pi_client import PiClient


log = logging.getLogger(__name__)


def main():
    rufus_client = RufusClient()
    pi_client = PiClient(rufus_client)
    pi_client.run()

if __name__ == '__main__':
    main()
