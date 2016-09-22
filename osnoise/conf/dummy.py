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

dummy_section = cfg.OptGroup('dummy_conf',
                                      title='OpenStack compute agents\' '
                                            'messaging options',
                                      help='Configuration options of '
                                           'the compute node agents\' RPC '
                                           'flows.')


dummy_options = [
    #exchange general properties
    cfg.StrOpt(
        'exchange_name',
        default='reply_q',
        help='Agent reply exchange name.'),
    cfg.StrOpt(
        'exchange_type',
        default='direct',
        help='Agent reply exchange type.'),

    #exchange specific properties
    cfg.BoolOpt(
        'is_passive',
        default=False,
        help='Exchange passive property.'),
    cfg.BoolOpt(
        'is_durable',
        default=False,
        help='Exchange durable property.'),
    cfg.BoolOpt(
        'is_auto_delete',
        default=False,
        help='Exchange auto-delete property.'),
    cfg.BoolOpt(
        'is_internal',
        default=False,
        help='Exchange internal property.'),
    cfg.ListOpt(
        'arguments',
        default=[],
        help='Exchange arguments.'),

    #message properties
    cfg.StrOpt(
        'routing_key',
        default='reply_q',
        help='Agent reply exchange routing key.'),
    cfg.StrOpt(
        'message_payload',
        default='payload',
        help='Agent reply message payload.'),


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
    conf.register_group(dummy_section)
    conf.register_opts(dummy_options, group=dummy_section)


def list_opts():
    return {dummy_section : dummy_options}