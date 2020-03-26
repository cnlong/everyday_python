from fabric.api import (local, put, abort, run, cd, task, execute, settings,
                        env, runs_once, lcd, sudo)
from fabric.contrib.console import confirm
from fabric.colors import green


env.user = 'root'
env.port = '22'
env.hosts = open('hosts').readlines()


@task
@runs_once
def test():
    local('tar -zvxf redis-5.0.8.tar.gz')
    with settings(warn_only=True), lcd('redis-5.0.8'):
        local('make distclean', capture=True)
        local('make', capture=True)
        result = local('make test', capture=True)
        if result.failed and not confirm('Test failed. Continue anyway?'):
            abort("Aborting at user request.")
        else:
            green("All tests passed without errors")
    with lcd("redis-5.0.8"):
        local("make clean")
    local('tar -czf redis-5.0.8.tar.gz redis-5.0.8')


@task
def deploy():
    put("redis-5.0.8.tar.gz", "/tmp/redis-5.0.8.tar.gz")
    with cd("/tmp"):
        run("tar -zxf redis-5.0.8.tar.gz")
        with cd("redis-5.0.8"):
            sudo("make distclean")
            sudo("make")
            sudo("make install")


@task
def clean_file():
    with cd("tmp"):
        sudo("rm -rf redis-5.0.8.tar.gz")
        sudo("rm -rf redis-5.0.8")


@task
def install():
    execute(test)
    execute(deploy)
    execute(clean_file)