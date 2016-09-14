# Copyright 2016 Orange
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Configuration of the following:
#   - System variable using defaults from osnoise.conf or config file
#     osnoise.conf
#   - Logging system based on logging configuration

import os
import logging as py_logging
import logging.handlers
from osnoise import conf
import osnoise.messaging

ENV_CONFIG_DIR_VAR = 'OSNOISE_PLACEMENT_CONFIG_DIR'
DEFAULT_CONFIG_DIR = '~' #for test only!!! Need to be changed; may be not
CONFIG_FILE = 'osnoise.conf'


CONF = conf.CONF

def _parse_args(default_config_files=None):
    CONF(project='osnoise',
         version='0.0.1',
         default_config_files=default_config_files)


def _get_config_file(env=None):
    if env is None:
        env = os.environ

    dirname = env.get(ENV_CONFIG_DIR_VAR, DEFAULT_CONFIG_DIR).strip()
    return os.path.join(dirname, CONFIG_FILE)


def _init_logger(config):
    # initialize the logging system
    LOG = py_logging.getLogger('osnoise')

    LOG_LEVELS = {'debug': py_logging.DEBUG,
                  'info': py_logging.INFO,
                  'warning': py_logging.WARNING,
                  'error': py_logging.ERROR,
                  'critical': py_logging.CRITICAL,
                  }
    log_level = LOG_LEVELS.get(config.log_level, py_logging.NOTSET)
    LOG.setLevel(log_level)
    log_handler=py_logging.handlers.RotatingFileHandler(config.log_dir +
                                                        config.log_file_name,
                                                        config.log_maxBytes,
                                                        config.log_backupCount,
                                                        )
    log_formatter = py_logging.Formatter('%(asctime)s - '
                                         '%(levelname)s '
                                         '[%(name)s] '
                                         '(pid=%(process)d) - '
                                         '%(message)s'
                                         )
    log_handler.setFormatter(log_formatter)
    LOG.addHandler(log_handler)

    #turn on the capture of warnings by logging
    logging.captureWarnings(True)

    LOG.debug('logging system is up.')


def init_config():
    # initialize the config system
    conf_file = _get_config_file()
    _parse_args(default_config_files=[conf_file])
    _init_logger(CONF)
    osnoise.messaging.init_messaging(CONF)
    return CONF