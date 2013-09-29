from fabric.api import *
from fabric.colors import *


@task
@roles('db')
def db():
    db_name = env.database['NAME']
    date_format_str = '`date +\%Y\%m\%d`'
    filename = '%s.%s.sql.bz2' % (env.application, date_format_str)
    dropdb = local('dropdb %s' % db_name)
    if dropdb.failed:
        print(red('%s does not exist' % db_name))
    get('%s/sql/%s' % env.remote_backups_path, filename)
    local('bzcat %s | psql %s > /dev/null' % filename, db_name)
    local('rm %s' % filename)


@task
@roles('web')
def media():
    local('rsync -vauz --delete %s/media/ media' % env.remote_backups_path)


@task
def search():
    local('python manage.py rebuild_index --noinput')


@task(default=True)
def all():
    execute(db)
    execute(media)
    if 'haystack' in settings.INSTALLED_APPS:
        execute(search)
