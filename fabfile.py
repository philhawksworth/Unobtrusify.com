# Fabric for deploying unobtrusify.com

from fabric.api import *
import os

# PROD = 'unobtrusify.com'
# DEST_PATH = '/var/www/unobtrusify.com'
# ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
# DEPLOY_PATH = os.path.join(ROOT_PATH, 'production_site')



# django.settings_module('ebay.config.europe.settings.local')
# from django.conf import settings

# env.project = "unobtrusify"

# SERVER
PRODUCTION = '46.51.184.117'


def production():
    """Production site"""
    env.alias = "production"
    env.hosts = [PRODUCTION]
    env.path = '/var/www/unobtrusify.com'
    env.user = 'ubuntu'
    env.key_filename  = '/Users/phil.hawksworth/.ssh/philhawksworth-aws.pem'
    env.apache = ['unobtrusify.com', ]
    env.release_path = "/var/releases/unobtrusify.com"


def deploy():
    """Deployment actions"""
    export_release()
    

def export_release():
    """Exports a release with the current time and date"""
    run('cd %s && git pull origin master' % env.release_path)
    run('cp -R %(release_path)s/deploy/* %(path)s' % env)


def copy_apache():
    """Copies the apache file to the appropriate location."""
    command = 'cp %s/current/etc/apache2/%s /etc/apache2/sites-available/'
    for config in env.apache:
        sudo(command % (env.path, config))


def restart():
    """Restarts the apache server"""
    copy_apache()
    sudo('/etc/init.d/apache2 restart')
