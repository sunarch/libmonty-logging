# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Basic library test - 2 - STDOUT_V1"""

# imports: project
import libmonty_logging.configs


def _reference_config() -> str:
    """Reference configuration for comparison"""

    return '''{
  "version": 1,
  "formatters": {
    "formatter1": {
      "format": "[%(asctime)s] [%(levelname)-8s] %(message)s",
      "datefmt": "%H:%M:%S"
    }
  },
  "handlers": {
    "handler1": {
      "class": "logging.StreamHandler",
      "level": "INFO",
      "formatter": "formatter1",
      "stream": "ext://sys.stdout"
    }
  },
  "loggers": {
    "root": {
      "level": "NOTSET",
      "handlers": [
        "handler1"
      ]
    }
  }
}'''


def create_config(**kwargs) -> tuple[str, dict]:
    """Create config"""

    config: dict = libmonty_logging.configs.get(libmonty_logging.configs.Config.STDOUT_V1)

    reference = _reference_config()

    return reference, config
