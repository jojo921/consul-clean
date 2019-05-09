#!/usr/bin/env python

from setuptools import setup
setup(name='consul-cleanup',
      version='1.0',
      description='Clean up critical services in consul',
      author='jojo921',
      author_email='935163873@qq.com',
      scripts=['consul-cleanup'],
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['python-consul==0.7.2', 'requests==2.18.4'],
     )