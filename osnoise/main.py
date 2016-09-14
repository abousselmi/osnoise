import osnoise.config as config
import osnoise.logger as logging

if __name__ == "__main__":
    CONF = config.init_config()

    # LOG = logging.getLogger(__name__)
    # LOG.info('log debug from main.')
    #
    # print 'dir2: %s' % CONF.log_dir
    # print 'l2 x type2: %s' % CONF.agents_messaging.nova_cpu_xname

    print 'rabbit_port: %s' %CONF.oslo_messaging_rabbit.rabbit_port