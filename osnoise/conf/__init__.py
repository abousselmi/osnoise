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

from oslo_config import cfg

from osnoise.conf import base
from osnoise.conf import compute
from osnoise.conf import paths
from osnoise.conf import rabbit


CONF = cfg.CONF


base.register_opts(CONF)
compute.register_opts(CONF)
rabbit.register_opts(CONF)
paths.register_opts(CONF)