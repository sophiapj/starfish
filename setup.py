#!/usr/bin/env python3
# -*- coding: utf-8 -*

'''
@Author: sophiapj
@Contact: sophiapj@163.com 
@File: setup.py.py
@Desc: setup
'''

import os
from setuptools import setup, find_packages
import codecs
import sys
import re

project_root = os.path.abspath(os.path.dirname(__file__))


def _get_here(fname):
    return os.path.join(os.path.dirname(__file__), fname)


def _get_long_description(fname, encoding='utf8'):
    return open(fname, 'r', encoding=encoding).read()


def read(*parts):
    return codecs.open(os.path.join(project_root, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup_options = dict(
    name='starfish',
    # keep in sync w/docs/conf.py manually for now, please!
    version=find_version("starfish", "__init__.py"),
    url='https://github.com/sophiapj/starfish',
    author='sophiapj',
    author_email='sophiapj@163.com',
    description="A python test framework",
    long_description=_get_long_description(fname=_get_here('README.rst')),
    packages=find_packages(exclude=['tests*']),
    package_data={'': ['README.rst', 'requirements.txt'], },
    platforms='any',
    zip_safe=True,
    license="Apache License 2.0",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)


if 'py2exe' in sys.argv:
    # This will actually give us a py2exe command.
    import py2exe
    # And we have some py2exe specific options.
    setup_options['options'] = {
        'py2exe': {
            'optimize': 0,
            'skip_archive': True,
            'dll_excludes': ['crypt32.dll'],
            'packages': ['docutils', 'urllib', 'httplib', 'HTMLParser',
                         'starfish', 'ConfigParser', 'xml.etree', 'pipes'],
        }
    }
    setup_options['console'] = ['bin/starfish']


setup(**setup_options)
