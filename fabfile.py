from __future__ import with_statement

import datetime
import os.path

from fabric.api import *


APP_NAME = 'tornado-base-app'
remote_egg_dir = '/tmp/'
eggname = ''

python_version = '2.7'


def get_egg_name():
    """Get the current egg name"""
    global eggname
    if not eggname:
        version = local('git describe --abbrev=4', capture=True)
        if version:
            version = '%s-%s' % (version, datetime.datetime.today().strftime('%Y%m%d'))
            eggname = APP_NAME + '-%s-py%s.egg' % (version.replace('-', '_'), python_version)
    return eggname

def build():
    """Build project into an egg file for distribution"""
    local('python' + python_version + ' setup.py bdist_egg')

def install():
    """Install egg file to target server"""
    remote_egg_path = os.path.join(remote_egg_dir, get_egg_name())
    sudo('easy_install -U %s' % remote_egg_path)
    sudo('rm %s' % remote_egg_path)

def copy():
    """Copy egg file to target server"""
    put(os.path.join('dist', get_egg_name()), remote_egg_dir)

def deploy():
    """Deploy app to servers"""
    build()
    copy()
    install()
