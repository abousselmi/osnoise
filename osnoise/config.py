#!/usr/bin/env python

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

import osnoise.common.config as config
import osnoise.conf.opts as opts


class ConfigBase(object):
    """The configuration class."""

    def __init__(self, confdir=None):
        if confdir:
            config.update_conf_dir(confdir=confdir)

        # init config
        self.conf = config.init_config()
        opts.list_opts()

    def get_conf(self):
        return self.conf
