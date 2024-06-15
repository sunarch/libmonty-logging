# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Default library test"""

# imports: library
from argparse import ArgumentParser

# imports: dependencies
import libmonty_logging
import libmonty_logging.version
import libmonty_logging.message as logging_message

MOCK_PROGRAM_NAME = libmonty_logging.version.PROGRAM_NAME + '-test'
MOCK_PROGRAM_VERSION = libmonty_logging.version.__version__


def main() -> None:
    """Main"""

    libmonty_logging.apply_default_console_and_file(MOCK_PROGRAM_NAME, MOCK_PROGRAM_VERSION)

    logging_message.program_header(MOCK_PROGRAM_NAME)

    parser = ArgumentParser(prog=MOCK_PROGRAM_NAME)

    parser.add_argument('--version',
                        help='Display version',
                        action='store_true',
                        dest='version')

    args = parser.parse_args()

    if args.version:
        print(f'{MOCK_PROGRAM_NAME} {MOCK_PROGRAM_VERSION}')


if __name__ == '__main__':
    main()
