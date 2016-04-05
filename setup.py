#!/usr/bin/env python
import uuid

from pip.req import parse_requirements
from setuptools import setup, find_packages

import version


def requirements(path):
    install_reqs = parse_requirements(path, session=uuid.uuid1())
    return [str(ir.req) for ir in install_reqs]


setup(
    name = 'tornado-base-app',
    version = version.get_git_version_or_default(),
    description = 'Tornado Base App',
    author = 'Ariel Barmat',
    author_email = 'abarmat@gmail.com',
    url = 'https://github.com/abarmat/tornado-base-app',
    packages = find_packages(exclude=['tests']),
    install_requires = requirements('requirements.txt'),
    scripts = [
        'server.py'
    ]
)
