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
import osnoise.common.logger as logging
import osnoise.core.messaging as messaging
import osnoise.core.publisher as publisher

import uuid
import sys

def main():
    print 'Starting..'

    global LOG

    try:
        # init config
        CONF = config.init_config()

        # init main log
        LOG = logging.getLogger(__name__)
        LOG.info('Start OSNoise')

        # init messaging config
        MSG = messaging.BasicMessaging(CONF)

        # init publisher and start publish
        PUB = publisher.Publisher(pub_id=uuid.uuid4(),
                                  duration=MSG.get_duration(),
                                  publish_rate=MSG.get_publish_rate(),
                                  channel=MSG.get_channel(),
                                  exchange=MSG.get_exchange(),
                                  routing_key=MSG.get_routing_key(),
                                  body=MSG.get_message_body(),
                                  properties=MSG.get_message_properties()
                                  )
        PUB.do_publish()

    except KeyboardInterrupt:
        LOG.info('Program interrupted by user. Stopping..')
        LOG.debug('Stop OSNoise')
        print 'Stopping..'

if __name__ == "__main__":
    main()
