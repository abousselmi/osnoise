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

compute_agents_section = cfg.OptGroup('agents_messaging',
                                      title='OpenStack compute agents\' '
                                            'messaging options',
                                      help='Configuration options of '
                                           'the compute node agents\' RPC '
                                           'flows.')


compute_agents_options = [
    cfg.StrOpt(
        'nova_cpu_xname',
        default='reply_q',
        help='Nova cpu agent reply exchange name.'),
    cfg.StrOpt(
        'nova_cpu_xtype',
        default='direct',
        help='Nova cpu agent reply exchange type.'),
    cfg.StrOpt(
        'nova_cpu_xrk',
        default='reply_q',
        help='Nova cpu agent reply exchange routing key.'),
    cfg.StrOpt(
        'nova_cpu_message_payload',
        default='payload',
        help='Nova cpu agent reply message payload.'),
    cfg.StrOpt(
        'neutron_l2agt_xname',
        default='reply_q',
        help='Neutron L2 agent reply exchange name.'),
    cfg.StrOpt(
        'neutron_l2agt_xtype',
        default='direct',
        help='Neutron L2 agent reply exchange type.'),
    cfg.StrOpt(
        'neutron_l2agt_xrk',
        default='reply_q',
        help='Neutron L2 agent reply exchange routing key.'),
    cfg.StrOpt(
        'neutron_l2agt_message_payload',
        default='payload',
        help='Neutron L2 agent reply message payload.'),

    # Message type property is mendatory. Without it,
    # rpc_common.deserialize_msg will raise a ValueError exception
    cfg.StrOpt(
        'message_type',
        default='application/json',
        help='Neutron L2 agent reply message type.'),
    cfg.IntOpt(
        'priority',
        default=0,
        help='AMQP message priority (See rabbitmq.com for more info).'),
    cfg.IntOpt(
        'delivery_mode',
        default=2,
        help='AMQP message delivery mode (See rabbitmq.com for more '
             'info).'),
    cfg.StrOpt(
        'message_encoding',
        default='utf-8',
        help='Neutron L2 agent reply message encoding.'),
]


def register_opts(conf):
    conf.register_group(compute_agents_section)
    conf.register_opts(compute_agents_options, group=compute_agents_section)


def list_opts():
    return {compute_agents_section : compute_agents_options}