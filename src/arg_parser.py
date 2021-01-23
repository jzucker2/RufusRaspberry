import argparse
from .version import version
from .constants import Constants
from .rufus_client import RufusClient

def create_argparser():
    parser = argparse.ArgumentParser(description='Pure python Raspberry Pi client for triggering Rufus activities.')
    parser.add_argument('--ip', type=str, default=Constants.DEFAULT_IP,
                        help='IP of Rufus server')
    parser.add_argument('activity', choices=RufusClient.all_activites(),
                        help='Activity for Rufus to execute')
    parser.add_argument('--version', action='version', version=version)
    return parser

