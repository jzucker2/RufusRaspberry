#!/usr/bin/env python3

import logging
from src import arg_parser
from src.rufus_client import RufusClient


log = logging.getLogger(__name__)


def main():
	parser = arg_parser.create_argparser()
	args = parser.parse_args()
	log.debug(f'Args: {args}')
	client = RufusClient(args.ip)
	response = client.request_activity(args.activity)
	log.info(f'Received response: {response}')
	print(f'Response ===> {response}')


if __name__ == '__main__':
	main()
