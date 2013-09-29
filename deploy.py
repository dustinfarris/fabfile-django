from fabric.api import *


def init_db():
    run('createdb %s' % env.database['NAME'])


def init_app():
    run('mkdir -p %s' % env.remote_sites_path)


def init_web():
    run('mkdir -p %s' % env.remote_media_path)


@task
def init():
    execute(init_db, roles='db')
    execute(init_app, roles='app')


@task
@roles('app')
def quick():
    with cd(env.remote_location):
        git_branch = run('git branch')
        if '* %s' % env.branch not in git_branch:
            abort('The server is not on the %s branch' % env.branch)
        git_status = run('git status')
        if 'Changes to be committed' in git_status:
            abort('There are uncommitted changes on the server.')

        run('git pull')

        with prefix('source env/bin/activate'):
            run('make update')


@task(default=True)
@roles('app')
def full():
    system_now = run('date +\%Y\%m\%d\%H\%M\%S')
    deploy_path = '%s/%s_%s' % (env.remote_sites_path, system_now, env.application)

    run('git clone %s %s' % (env.repo_url, deploy_path))

    with cd(deploy_path):
        run('git checkout %s' % env.branch)
        run('ln -sf %s media' % env.remote_media_path)
        run('virtualenv env')

        with prefix('source env/bin/activate'):
            run('make install-core')
            run('make update')

    run('ln -sfn %s %s' % (deploy_path, env.remote_location))
    execute('restart')

