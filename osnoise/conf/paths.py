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

# Based on nova/conf/paths.py
import os
import sys

from oslo_config import cfg


global_paths_options = [
    cfg.StrOpt('pybasedir',
               default=os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                    '../../')),
               help='The directory where the OSNoise python modules are '
                    'installed.'),
    cfg.StrOpt('bindir',
               default=os.path.join(sys.prefix, 'local', 'bin'),
               help='The directory where the OSNoise binaries are installed.'),
    cfg.StrOpt('state_path',
               default='$pybasedir',
               help='The top-level directory for maintaining OSNoise\'s '
                    'state.'),
]


def basedir_def(*args):
    """Return an uninterpolated path relative to $pybasedir."""
    return os.path.join('$pybasedir', *args)


def bindir_def(*args):
    """Return an uninterpolated path relative to $bindir."""
    return os.path.join('$bindir', *args)


def state_path_def(*args):
    """Return an uninterpolated path relative to $state_path."""
    return os.path.join('$state_path', *args)


def register_opts(conf):
    conf.register_opts(global_paths_options)


def list_opts():
    return {"DEFAULT" : global_paths_options}