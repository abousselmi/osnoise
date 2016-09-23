
from osnoise.core import messaging
from osnoise.common import logger as logging
import threading
import time

LOG = logging.getLogger(__name__)


def do_thread(function):
    def wrapper(*args, **kwargs):
        threading.Thread(target=function, args=args, kwargs=kwargs).start()

    return wrapper

class Publisher(object):
    """The publisher class"""

    def __init__(self, pub_id=None, duration=None, publish_rate=None,
                 channel=None, exchange=None, routing_key=None, body=None,
                 properties=None):
        self._stop = threading.Event()
        self.pub_id = pub_id
        self.duration = duration
        self.publish_rate = publish_rate
        self.channel = channel
        self.exchange_name = exchange
        self.routing_key = routing_key
        self.message_payload = body
        self.message_properties = properties

        self.interval = 0

    def _delay_publish(self, message_count, interval):
        elapsed_time = int(round(time.time() * 1000)) - interval
        pause_time = message_count * 1000 / self.publish_rate - \
                     elapsed_time if self.publish_rate != 0 else 0

        if pause_time > 0:
            try:
                time.sleep(pause_time/1000)
            except Exception:
                LOG.error('Caught exception when trying to sleep.')

    @do_thread
    def _update_interval(self, current_time):
        while True:
            if current_time - self.interval >= 1000:
                # new one second interval
                self.interval += 1000

    @do_thread
    def do_publish(self):
        LOG.debug('Start publishing..')
        start_time = current_time = interval = int(round(time.time() * 1000))
        self.interval = interval
        message_count = 0

        try:
            while (self.duration == 0 or current_time <
                    start_time + self.duration*1000):
                #keep up with the publish rate
                self._delay_publish(message_count=message_count,
                                    interval=interval)
                #publish
                self.channel.basic_publish(exchange=self.exchange_name,
                                           routing_key=self.routing_key,
                                           body=self.message_payload,
                                           properties=self.message_properties
                                           )
                message_count += 1
                current_time = int(round(time.time() * 1000))
                LOG.debug('[PUB] %s' %self.message_payload)
            LOG.info('Total messages %s' %(message_count-1))
        except IOError as ex:
            LOG.error('I/O error({0}): {1}'.format(ex.errno, ex.strerror))

    def do_stop(self):
        LOG.debug('Stop publishing..')
        self._stop.set()
