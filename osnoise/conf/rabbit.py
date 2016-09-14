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

# Full list can be found at oslo_messaging/_drivers/impl_rabbit.py
rabbitmq_section = cfg.OptGroup('oslo_messaging_rabbit',
                                title='RabbitMQ options',
                                help='Configuration section of RabbitMQ.')


rabbit_options = [
    cfg.StrOpt('kombu_ssl_version',
               default='',
               deprecated_group='DEFAULT',
               help='SSL version to use (valid only if SSL enabled). '
                    'Valid values are TLSv1 and SSLv23. SSLv2, SSLv3, '
                    'TLSv1_1, and TLSv1_2 may be available on some '
                    'distributions.'
               ),
    cfg.StrOpt('kombu_ssl_keyfile',
               default='',
               deprecated_group='DEFAULT',
               help='SSL key file (valid only if SSL enabled).'),
    cfg.StrOpt('kombu_ssl_certfile',
               default='',
               deprecated_group='DEFAULT',
               help='SSL cert file (valid only if SSL enabled).'),
    cfg.StrOpt('kombu_ssl_ca_certs',
               default='',
               deprecated_group='DEFAULT',
               help='SSL certification authority file '
                    '(valid only if SSL enabled).'),
    cfg.FloatOpt('kombu_reconnect_delay',
                 default=1.0,
                 deprecated_group='DEFAULT',
                 help='How long to wait before reconnecting in response to an '
                      'AMQP consumer cancel notification.'),
    cfg.StrOpt('kombu_compression',
               help="EXPERIMENTAL: Possible values are: gzip, bz2. If not "
                    "set compression will not be used. This option may not "
                    "be available in future versions."),
    cfg.IntOpt('kombu_missing_consumer_retry_timeout',
               deprecated_name="kombu_reconnect_timeout",
               default=60,
               help='How long to wait a missing client before abandoning to '
                    'send it its replies. This value should not be longer '
                    'than rpc_response_timeout.'),
    cfg.StrOpt('kombu_failover_strategy',
               choices=('round-robin', 'shuffle'),
               default='round-robin',
               help='Determines how the next RabbitMQ node is chosen in case '
                    'the one we are currently connected to becomes '
                    'unavailable. Takes effect only if more than one '
                    'RabbitMQ node is provided in config.'),
    cfg.StrOpt('rabbit_host',
               default='localhost',
               deprecated_group='DEFAULT',
               deprecated_for_removal=True,
               deprecated_reason="Replaced by [DEFAULT]/transport_url",
               help='The RabbitMQ broker address where a single node is '
                    'used.'),
    cfg.PortOpt('rabbit_port',
                default=5673,
                deprecated_group='DEFAULT',
                deprecated_for_removal=True,
                deprecated_reason="Replaced by [DEFAULT]/transport_url",
                help='The RabbitMQ broker port where a single node is used.'),
    cfg.ListOpt('rabbit_hosts',
                default=['$rabbit_host:$rabbit_port'],
                deprecated_group='DEFAULT',
                deprecated_for_removal=True,
                deprecated_reason="Replaced by [DEFAULT]/transport_url",
                help='RabbitMQ HA cluster host:port pairs.'),
    cfg.BoolOpt('rabbit_use_ssl',
                default=False,
                deprecated_group='DEFAULT',
                help='Connect over SSL for RabbitMQ.'),
    cfg.StrOpt('rabbit_userid',
               default='guest',
               deprecated_group='DEFAULT',
               deprecated_for_removal=True,
               deprecated_reason="Replaced by [DEFAULT]/transport_url",
               help='The RabbitMQ userid.'),
    cfg.StrOpt('rabbit_password',
               default='guest',
               deprecated_group='DEFAULT',
               deprecated_for_removal=True,
               deprecated_reason="Replaced by [DEFAULT]/transport_url",
               help='The RabbitMQ password.',
               secret=True),
    cfg.StrOpt('rabbit_login_method',
               default='AMQPLAIN',
               deprecated_group='DEFAULT',
               help='The RabbitMQ login method.'),
    cfg.StrOpt('rabbit_virtual_host',
               default='/',
               deprecated_group='DEFAULT',
               deprecated_for_removal=True,
               deprecated_reason="Replaced by [DEFAULT]/transport_url",
               help='The RabbitMQ virtual host.'),
    cfg.IntOpt('rabbit_retry_interval',
               default=1,
               help='How frequently to retry connecting with RabbitMQ.'),
    cfg.IntOpt('rabbit_retry_backoff',
               default=2,
               deprecated_group='DEFAULT',
               help='How long to backoff for between retries when connecting '
                    'to RabbitMQ.'),
    cfg.IntOpt('rabbit_interval_max',
               default=30,
               help='Maximum interval of RabbitMQ connection retries. '
                    'Default is 30 seconds.'),
    cfg.IntOpt('rabbit_max_retries',
               default=0,
               deprecated_for_removal=True,
               deprecated_group='DEFAULT',
               help='Maximum number of RabbitMQ connection retries. '
                    'Default is 0 (infinite retry count).'),
    cfg.BoolOpt('rabbit_ha_queues',
                default=False,
                deprecated_group='DEFAULT',
                help='Try to use HA queues in RabbitMQ (x-ha-policy: all). '
                     'If you change this option, you must wipe the RabbitMQ '
                     'database. In RabbitMQ 3.0, queue mirroring is no longer '
                     'controlled by the x-ha-policy argument when declaring a '
                     'queue. If you just want to make sure that all queues (except '
                     ' those with auto-generated names) are mirrored across all '
                     'nodes, run: '
                     """\"rabbitmqctl set_policy HA '^(?!amq\.).*' """
                     """'{"ha-mode": "all"}' \""""),
    cfg.IntOpt('rabbit_transient_queues_ttl',
               min=1,
               default=1800,
               help='Positive integer representing duration in seconds for '
                    'queue TTL (x-expires). Queues which are unused for the '
                    'duration of the TTL are automatically deleted. The '
                    'parameter affects only reply and fanout queues.'),
    cfg.IntOpt('rabbit_qos_prefetch_count',
               default=0,
               help='Specifies the number of messages to prefetch. Setting to '
                    'zero allows unlimited messages.'),
    cfg.IntOpt('heartbeat_timeout_threshold',
               default=60,
               help="Number of seconds after which the Rabbit broker is "
                    "considered down if heartbeat's keep-alive fails "
                    "(0 disable the heartbeat). EXPERIMENTAL"),
    cfg.IntOpt('heartbeat_rate',
               default=2,
               help='How often times during the heartbeat_timeout_threshold '
                    'we check the heartbeat.'),
]


def register_opts(conf):
    #conf.register_group(rabbitmq_section)
    conf.register_opts(rabbit_options, group=rabbitmq_section)


def list_opts():
    return {rabbitmq_section : rabbit_options}