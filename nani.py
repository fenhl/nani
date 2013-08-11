#!/usr/bin/env python3
"""Information overview for command line tools.

Usage:
  nani <command>
  nani -h | --help
  nani --version

Options:
  -h, --help  Print this message and exit.
  --version   Print version info and exit.
"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='nani 0.1.0')
    #TODO some actual functionality
