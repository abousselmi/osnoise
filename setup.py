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

from distutils.core import setup
from setuptools import find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENCE.txt') as f:
    license = f.read()

setup(
    name='osnoise',
    version='0.0.1dev0',
    description='OpenStack compute agents (nova_cpu and neutron_l2agt) tcp '
                'connection loader.',
    long_description=readme,
    author='Ayoub Bousselmi',

    license=license,
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
)
