# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Basic library test"""

# imports: library
import json

# imports: dependencies
import libmonty_logging
import libmonty_logging.configs
import libmonty_logging.paths
import libmonty_logging.version


MOCK_PROGRAM_NAME = libmonty_logging.version.PROGRAM_NAME + '-test'
MOCK_PROGRAM_VERSION = libmonty_logging.version.__version__


def reference_config(log_file_path: str) -> str:
    """Reference configuration for comparison"""

    return '''{
  "version": 1,
  "formatters": {
    "formatter1": {
      "format": "[%(asctime)s] [%(levelname)-8s] %(message)s",
      "datefmt": "%H:%M:%S"
    },
    "formatter2": {
      "format": "[%(asctime)s] [%(levelname)-8s] %(message)s"
    }
  },
  "handlers": {
    "handler1": {
      "class": "logging.StreamHandler",
      "level": "INFO",
      "formatter": "formatter1",
      "stream": "ext://sys.stdout"
    },
    "handler2": {
      "class": "logging.FileHandler",
      "level": "INFO",
      "formatter": "formatter2",
      "filename": "''' + log_file_path + '''",
      "mode": "w",
      "encoding": "UTF-8"
    }
  },
  "loggers": {
    "root": {
      "level": "NOTSET",
      "handlers": [
        "handler1",
        "handler2"
      ]
    }
  }
}'''


def line_display_format(line: str) -> str:
    """Create a display format of a config line for comparison"""

    return (
        line
        .replace(' ', '·')
        .replace('\t', '↹')
        .replace('\r', '⤶')
        .replace('\n', '⤶')
    )


def main() -> None:
    """Main"""

    log_file_path = libmonty_logging.paths.get(libmonty_logging.paths.LogDirPath.XDG_STATE_HOME_WITH_NAME_V1,
                                               libmonty_logging.paths.LogFilename.NAME_DASH_VERSION_V1,
                                               program_name=MOCK_PROGRAM_NAME,
                                               program_version=MOCK_PROGRAM_VERSION)
    config = libmonty_logging.configs.get(libmonty_logging.configs.Config.STDOUT_AND_FILE_V1,
                                          log_file_path=log_file_path)

    libmonty_logging.apply_config(config)

    reference: str = reference_config(log_file_path)
    generated: str = json.dumps(config, indent=2)
    is_equal: bool = generated == reference

    if is_equal:
        print('Generated and reference versions are equal')
    else:
        print()
        print(f'{"  DIFFERENCE  ":=^80}')

        reference_lines: list[str] = reference.split('\n')
        generated_lines: list[str] = generated.split('\n')

        for i_line, ref_and_gen in enumerate(zip(reference_lines, generated_lines)):
            line_ref, line_gen = ref_and_gen
            if line_ref != line_gen:
                print()
                print('Line', i_line)
                print('REF:', line_display_format(line_ref))
                print('GEN:', line_display_format(line_gen))

        print()
        print(f'{"  RESULT  ":=^80}')
        print()
        print('PROBLEM: Generated and reference versions are NOT equal')


if __name__ == '__main__':
    main()
