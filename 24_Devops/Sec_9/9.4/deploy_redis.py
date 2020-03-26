"""
通常情况下，fabfile不能带注释文档信息，否则会报错
"""
from fabric.api import (local, put, abort, run, cd, task, execute, settings,
                        env, runs_once, lcd, sudo)
from fabric.contrib.console import confirm
from fabric.colors import green


# 设置环境变量
env.user = 'root'
env.port = '22'
env.hosts = open('hosts').readlines()


# 定义本地文件的检查任务，并且只执行一次
@task
@runs_once
def test():
    # 如果有执行失败，仍然继续不终止
    local('tar -zvxf redis-5.0.8.tar.gz')
    with settings(warn_only=True), lcd('redis-5.0.8'):
        local('make distclean', capture=True)
        local('make', capture=True)
        # 运行测试，测试redis的功能是否正常,获取测试结果
        result = local('make test', capture=True)
        # 如果测试失败，则提示信息，如果输入yes，则继续忽略报错，如果输入no则终止操作
        if result.failed and not confirm('Test failed. Continue anyway?'):
            abort("Aborting at user request.")
        # 测试成功，打印测试信息
        else:
            green("All tests passed without errors")
    # 清除缓存
    with lcd("redis-5.0.8"):
        local("make clean")
    # 打包源码包
    local('tar -czf redis-5.0.8.tar.gz redis-5.0.8')


# 上传部署文档
@task
def deploy():
    # 上传文件
    put("redis-5.0.8.tar.gz", "/tmp/redis-5.0.8.tar.gz")
    with cd("/tmp"):
        # 解压文件
        run("tar -zxf redis-5.0.8.tar.gz")
        with cd("redis-5.0.8"):
            sudo("make distclean")
            sudo("make")
            # 管理员权限执行安装
            sudo("make install")


# 清除安装的源文件
@task
def clean_file():
    with cd("/tmp"):
        sudo("rm -rf redis-5.0.8.tar.gz")
        sudo("rm -rf redis-5.0.8")


# 定义任务总列表
@task
def install():
    execute(test)
    execute(deploy)
    execute(clean_file)