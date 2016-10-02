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

tsunami_section = cfg.OptGroup('tsunami_conf',
                               title='Tsunami test config.'
                               )

tsunami_options = [
    # tsunami wave message count, used to test in how much time
    # tsunami_message_count messages are published.
    cfg.IntOpt('tsunami_message_count',
               default=10000,
               help='Published messages count.'),
]


def register_opts(conf):
    conf.register_group(tsunami_section)
    conf.register_opts(tsunami_options, group=tsunami_section)


def list_opts():
    return {tsunami_section : tsunami_options}
