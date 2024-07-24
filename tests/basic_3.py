# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Basic library test - 3 - FILE_V1"""

# imports: project
import libmonty_logging
import libmonty_logging.configs
import libmonty_logging.paths
import libmonty_logging.version


def _reference_config(log_file_path: str) -> str:
    """Reference configuration for comparison"""

    return '''{
  "version": 1,
  "formatters": {
    "formatter2": {
      "format": "[%(asctime)s] [%(levelname)-8s] %(message)s"
    }
  },
  "handlers": {
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
        "handler2"
      ]
    }
  }
}'''


def create_config(**kwargs) -> tuple[str, dict]:
    """Create config"""

    log_file_path = libmonty_logging.paths.get(
        libmonty_logging.paths.LogDirPath.XDG_STATE_HOME_WITH_NAME_V1,
        libmonty_logging.paths.LogFilename.NAME_DASH_VERSION_V1,
        program_name=kwargs['program_name'],
        program_version=kwargs['program_version']
    )

    config: dict = libmonty_logging.configs.get(
        libmonty_logging.configs.Config.FILE_V1,
        log_file_path=log_file_path
    )

    reference = _reference_config(log_file_path)

    return reference, config
