#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description': 'My Project',
    'author': 'Matthew Trisoline',
    'url': 'Not There Yet'
    'download_url': 'Not ready for download yet.'
    'author_email': 'Ya...'
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
]

setup(**config)
