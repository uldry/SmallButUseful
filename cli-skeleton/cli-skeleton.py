#!/usr/bin/env python

import time
import argh
from tqdm import tqdm, trange
import logging
import os, sys
from datetime import datetime, date

levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}


# Required positional argument, not a big fan.
@argh.arg('reqpos', help='positional argument', type=int)
# A 'required option', those have are explicitly named, a must when your argument list is a mile long
@argh.arg('--req_arg1', required=True, help='required option arg1')
# Optional integer here
@argh.arg('--opt_arg2', default=10, help='optional arg2', type=int)
# a simple flag
@argh.arg('--opt_flag', default=False, help='optional flag')
# This one has a shortcut, a default value and a list to choose from that will be enforced
@argh.arg('-l', '--loglevel', choices=['info', 'warn', 'debug', 'error', 'critical'], default='warning')
def main(**kwargs):
    """
    This is the main function.
    It will create a log file using the script name and the timestamp
    Using hours, minutes and seconds in the timestamp may be required in some cases.

    A progress bar will be set by opt-arg2
    """
    loglevel = kwargs['loglevel']
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    scriptLogFile = "./" + os.path.basename(sys.argv[0]).split(".")[0] + "_" + timestamp + ".log"

    level = levels.get(loglevel.lower())

    logging.basicConfig(level=level, filename=scriptLogFile, filemode='w',
                        format='%(asctime)s - %(levelname)s - %(funcName)s() - L%(lineno)s - %(message)s')
    logging.info('This is just to tell we started')
    print("\nHere are all the arguments:")
    print(kwargs)
    logging.debug(kwargs)

    print("Now, let's use opt_arg2 for a progress bar")
    t = trange(kwargs['opt_arg2'])
    for i in t:
        t.set_description(f"on iter {i}")
        time.sleep(0.2)
        logging.debug("Just slept 200ms x %s" % (i + 1))
    print()
    logging.info('Goodbye')


@argh.arg('otherpos', help='positional argument', type=str)
@argh.arg('--opt_arg', default=False, help='optional arg')
def other(**kwargs):
    """
    This is the other function.
    No logging here.
    """
    print("\nHere are all the arguments:")
    print(kwargs)
    print()


if __name__ == '__main__':
    # Single function
    # argh.dispatch_command(main)
    # Multiple functions dispatch
    argh.dispatch_commands([main, other])
