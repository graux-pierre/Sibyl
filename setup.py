#! /usr/bin/env python

from distutils.core import setup, Extension

setup(
    name='Sibyl',
    description='API bruteforcing tool',
    packages=['sibyl',
              'sibyl/abi',
              'sibyl/actions',
              'sibyl/heuristics',
              'sibyl/test',
              'sibyl/learn/generator',
              'sibyl/learn/tracer'
          ],
    scripts=['bin/sibyl'],
    data_files=['']
)
