from fabric.api import env, task
from fabric.contrib import django

from fabfile import deploy, refresh, restart, stage, sync, topic


# ENVIRONMENT

env.application = 'plumradio'
env.repo_url = 'git@github.com:phazemedia/plumradio.git'
env.production_branch = 'master'
env.staging_branch = 'staging'

django.project(env.application)


# SERVER CONFIGURATION

@task
def staging():
    env.branch = env.staging_branch
    env.roledefs = {
            'app': ['web@162.209.99.49'],
            'db': ['web@162.209.99.49'],
            }


@task
def production():
    env.branch = env.production_branch
    env.roledefs = {
            'app': ['web@192.237.219.246'],
            'db': ['web@192.237.219.246'],
            }


env.remote_location = '/var/www/%s' % env.application
env.remote_sites_path = '/var/www/.sites'
env.remote_media_path = '/var/www/.media/%s' % env.application
env.remote_backups_path = '/var/backups'


# DATABASE

from django.conf import settings
env.database = settings.DATABASES['default']


# MISCELLANEOUS SETTINGS

env.colorize_errors = True
