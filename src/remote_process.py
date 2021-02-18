import logging
from .rufus_client import RufusClient
from .pi_client import PiClient
from .arg_parser import create_argparser
from .utils import get_log_level


log = logging.getLogger(__name__)


def run_remote(config_class):
    arg_parser = create_argparser()
    args = arg_parser.parse_args()
    log_level = get_log_level(args.debug)
    logging.basicConfig(level=log_level)
    log.info(f'Set log_level to {log_level}')
    rufus_client = RufusClient(ip=args.ip)
    living_room_config = config_class()
    pi_client = PiClient(rufus_client, living_room_config, debug=args.debug, reverse_rotary_encoder=args.reverse_rotary_encoder)
    # run as well
    pi_client.run()
