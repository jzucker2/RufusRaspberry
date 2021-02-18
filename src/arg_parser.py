import argparse
from .version import version
from .constants import Constants
from .activities import Activities

def create_argparser(include_activity_choices=False):
    parser = argparse.ArgumentParser(description='Pure python Raspberry Pi client for triggering Rufus activities.')
    parser.add_argument('--ip', type=str, default=Constants.DEFAULT_IP,
                        help='IP of Rufus server')
    parser.add_argument('--reverse-rotary-encoder', action='store_true',
                        help='Reverse rotary encoder flag (in case of weird install).')
    if include_activity_choices:
        parser.add_argument('activity', choices=Activities.all_activity_names(),
                            help='Activity for Rufus to execute')
    parser.add_argument('--debug', '-d', action='store_true', help='Turn on the debug flag (will ensure Raspberry Pi only logs')
    parser.add_argument('--version', action='version', version=version)
    return parser

