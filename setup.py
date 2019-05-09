#!/usr/bin/env python

from setuptools import setup
setup(name='consul-clear',
      version='1.0',
      description='Clean up critical services in consul',
      author='jojo921',
      author_email='935163873@qq.com',
      scripts=['consul-clear.py'],
      url='https://github.com/jojo921/consul-clear.git',
      install_requires=['python-consul==0.7.2', 'requests==2.18.4'],
     )