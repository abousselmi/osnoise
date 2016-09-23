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

import pika
import pika.credentials as pika_credentials
import pika.spec
import time
from threading import Thread

import osnoise.conf
import osnoise.config as cfg
import osnoise.logger as logging


CONF = osnoise.conf.CONF
LOG = logging.getLogger(__name__)


class BasicPublisher(object):
    """The publisher class of dummy messages"""

    def __init__(self, conf):
        # rabbitmq config options
        LOG.debug('Loading messaging configuration.')
        if conf.rabbit_conf.rabbit_transport:
            self.rabbitTransport   = conf.rabbit_conf.rabbit_transport

        self.rabbitUID          = conf.rabbit_conf.rabbit_userid
        self.rabbitPass         = conf.rabbit_conf.rabbit_password
        self.rabbitHost         = conf.rabbit_conf.rabbit_host
        self.rabbitPort         = conf.rabbit_conf.rabbit_port
        self.rabbitVHost        = conf.rabbit_conf.rabbit_virtual_host
        self.rabbitHosts        = conf.rabbit_conf.rabbit_hosts
        self.rabbitUseSSL       = conf.rabbit_conf.rabbit_use_ssl
        self.rabbitLoginMethod  = conf.rabbit_conf.rabbit_login_method

        #pika config options
        self.channel_max        = conf.rabbit_conf.pika_channel_max
        self.frame_max          = conf.rabbit_conf.pika_frame_max
        self.heartbeat_rate     = conf.rabbit_conf.heartbeat_rate
        self.connection_attemps = conf.rabbit_conf.rabbit_max_retries
        self.retry_delay        = conf.rabbit_conf.rabbit_retry_interval
        self.socket_timeout     = conf.rabbit_conf.pika_socket_timeout
        self.pika_locale        = conf.rabbit_conf.pika_set_locale

        # message publisher config options
        self.exchange_name      = conf.dummy_conf.exchange_name
        self.exchange_type      = conf.dummy_conf.exchange_type
        self.is_passive         = conf.dummy_conf.is_passive
        self.is_durable         = conf.dummy_conf.is_durable
        self.is_auto_delete     = conf.dummy_conf.is_auto_delete
        self.is_internal        = conf.dummy_conf.is_internal
        self.arguments          = conf.dummy_conf.arguments
        self.routing_key        = conf.dummy_conf.routing_key
        self.message_payload    = conf.dummy_conf.message_payload

        self.publish_rate       = conf.dummy_conf.publish_rate
        self.noise_dureation    = conf.dummy_conf.duration

        content_type       = conf.dummy_conf.message_type
        content_encoding   = conf.dummy_conf.message_encoding
        priority           = conf.dummy_conf.priority
        delivery_mode      = conf.dummy_conf.delivery_mode
        user_id            = self.rabbitUID
        app_id             = cfg.PRODUCT_NAME
        message_id         = app_id+'_message'

        self.properties = pika.spec.BasicProperties(
            content_type=content_type,
            content_encoding=content_encoding,
            priority=priority,
            delivery_mode=delivery_mode,
            user_id=user_id,
            app_id=app_id,
            message_id=message_id
        )

        #init connection
        self._init_connection()

    def _init_connection(self):
        LOG.debug('Initializing connection to rabbitmq node.')
        #construct credentials
        credentials = pika_credentials.PlainCredentials(
            username=self.rabbitUID,
            password=self.rabbitPass
        )
        parameters = pika.ConnectionParameters(
            host=self.rabbitHost,
            port=self.rabbitPort,
            virtual_host=self.rabbitVHost,
            credentials=credentials,
            channel_max=self.channel_max,
            frame_max=self.frame_max,
            heartbeat_interval=self.heartbeat_rate,
            connection_attempts=self.connection_attemps,
            retry_delay=self.retry_delay,
            socket_timeout=self.socket_timeout,
            locale=self.pika_locale
        )
        self.connection = pika.BlockingConnection(parameters=parameters)
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange_name,
                                      exchange_type=self.exchange_type,
                                      passive=self.is_passive,
                                      durable=self.is_durable,
                                      auto_delete=self.is_auto_delete,
                                      internal=self.is_internal,
                                      arguments=self.arguments
                                      )


    def start_publishing(self):
        LOG.debug('Start publishing very noisy messages :D.')
        if self.noise_dureation != 0:
            t_end = time.time() + self.noise_dureation
            while time.time() < t_end:
                self.channel.basic_publish(exchange=self.exchange_name,
                                           routing_key=self.routing_key,
                                           body=self.message_payload,
                                           properties=self.properties)
                time.sleep(1)
                LOG.debug('Publishing message: %s' %self.message_payload)
        else:
            try:
                while True:
                    self.channel.basic_publish(exchange=self.exchange_name,
                                               routing_key=self.routing_key,
                                               body=self.message_payload,
                                               properties=self.properties)
                    time.sleep(1)
                    LOG.debug('Publishing message: %s' % self.message_payload)
            except KeyboardInterrupt:
                LOG.debug('Program interrupted by user. Stopping..')
                print 'program interrupted by user. Stopping..'

    def close_connection(self):
        if self.connection:
            self.connection.close()
            LOG.info('Connection to RabbitMQ is closed.')
        else:
            LOG.warning('No connection to close.')


            # class infinite_pablish(Thread):
            #     def run(self):


