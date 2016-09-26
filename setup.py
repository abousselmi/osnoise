from distutils.core import setup
from setuptools import find_packages

setup(
    name='OSNoise',
    version='0.0.1dev',
    description='OpenStack compute agents (nova_cpu and neutron_l2agt) tcp '
                'connection loader.',

    author='Ayoub BOUSSELMI',

    license='Apache Software License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Testers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='wan amqp openstack rabbitmq messaging',
    packages=find_packages(exclude=['osnoise.test',]),

    install_requires=['oslo.config', 'pika'],
    entry_points={
        'console_script': [
            'osnoise.conf=osnoise.conf.opts:list_opts',
            'osnoise=osnoise.main:main'
        ],
    },
)