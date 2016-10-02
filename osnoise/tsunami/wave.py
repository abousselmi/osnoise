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

import osnoise.config as config
import osnoise.common.logger as logging
import osnoise.core.messaging as messaging

import time


class Wave(object):
    """Tsunami wave generation class."""

    def run(self, confdir=None):
        try:
            global LOG
            c = config.ConfigBase(confdir=confdir)
            conf = c.get_conf()

            # init tsunami log
            LOG = logging.getLogger(__name__)
            LOG.info('Start Tsunami..')
            print 'Start Tsunami..'
            # init messaging config
            msg = messaging.BasicMessaging(conf)

            channel = msg.get_channel()

            counter = 0
            start_time = time.time()

            while counter < msg.get_tsunami_message_count():
                channel.basic_publish(exchange=msg.get_exchange(),
                                      routing_key=msg.get_routing_key(),
                                      body=msg.get_message_body(),
                                      properties=msg.get_message_properties()
                                      )
                counter += 1
            print 'This wave took %s seconds to publish %s messages.' % (
                time.time()-start_time, msg.get_tsunami_message_count())
            LOG.info('This wave took %s seconds to publish %s messages.' % (
                time.time()-start_time, msg.get_tsunami_message_count()))
            LOG.info('Stop Tsunami..')
            print 'Stop Tsunami..'
        except KeyboardInterrupt:
            LOG.warning('Program interrupted by user..')
            LOG.info('Stopping tsunami..')
