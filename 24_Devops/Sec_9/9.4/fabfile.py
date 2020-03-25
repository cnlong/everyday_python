from fabric.api import run, sudo, env, cd, hide, settings, task, \
    hosts, roles, runs_once, execute
from fabric.utils import puts
from fabric.colors import blue


env.hosts = ['192.168.6.162', '192.168.6.163']
env.port = 22
env.user = 'root'
env.roledefs = {
    'node01': ['192.168.6.162', ],
    'node02': ['192.168.6.163', ],
    'k8snode': ['192.168.6.162', '192.168.6.163']
}


@hosts('192.168.6.163')
def hostname():
    run('hostname')


@roles('node01')
def ls(path='.'):
    run('ls {}'.format(path))
    puts("execute successful!")
    print(blue('hahaha'))


def tail(path='/etc/passwd', line=10):
    sudo('tail -n {0} {1}'.format(line, path))


# @task
def chd(path='.'):
    with cd(path):
        run('ls')


def my_task():
    with settings(warn_only=True):
        run('rm /tmp/notexists')
    with hide('running', 'stdout', 'stderr'):
        run('ls /var/log')


# @runs_once
# def hello():
#     print('Hello, World')
#
#
# @task
# def test():
#     execute(hello)
#     execute(hello)

