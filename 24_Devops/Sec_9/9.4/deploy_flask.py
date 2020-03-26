"""因为没有测试机器，本脚本暂未测试"""
from fabric.api import *
from fabric.colors import red, green, yellow
from fabric.contrib.files import exists


# 设置环境变量
env.user = 'root'
env.port = '2092'
env.roledefs = {'web': ['192.168.6.162', '192.168.6.163'],
                'db': ['192.168.6.167']}


# 确认redis是否安装
def is_redis_installed():
    # 忽略所有输出,告警输出继续
    with settings(hide('everything'), warn_only=True):
        # 查询端口是否存在
        result = run('netstat -tl|grep -w 6379')
        # 如果存在执行返回0，如果不存在执行命令行返回非0
        # 返回0，函数返回True，不返回0，函数返回False
        return result.return_code == 0


# yum安装redis
def install_redis():
    sudo('yum install redis-server')


# 修改配置文件
def change_redis_conf():
    sudo("sed -i 's/bind 127.0.0.1/bind 0.0.0.0' /etc/redis/redis.conf")


# 重启redis服务。设置伪终端，方式程序退出，导致重启进程退出
def reboot_redis():
    sudo('/etc/init.d/redis-server restart', pty=False)


# db的role服务器部署redis
@task
@roles('db')
def deploy_db():
    # 先判断是否安装过
    if is_redis_installed():
        print(yellow("redis was successfully installed!"))
    # 如果没有安装过，就执行安装相关的步骤
    else:
        install_redis()
        change_redis_conf()
        reboot_redis()
        print(green('redis has successfully installed!'))


# 判断python库是否安装过，通过尝试导入的方式验证
def is_python_package_installed(package):
    with settings(hide('everything'), warn_only=True):
        result = run('python -c import {0}'.format(package))
        # 如果执行成功返回0，如果执行失败命令行返回非0
        # 返回0，函数返回True，不返回0，函数返回False
        return result.return_code == 0


# 安装python库
def install_python_package(package):
    sudo("pip install {0}".format(package))



# 根据是否安装的情况安装库
def pip_install_if_nedd(package):
    if not is_python_package_installed(package):
        install_python_package(package)
        print(green('{0} has installed'.format(package)))
    else:
        print(yellow('{0} was installed'.format(package)))


# 安装项目所需的库,gunicorn启动服务，访问redis数据库的驱动
def install_package():
    for package in ['gunicorn', 'flask', 'redis']:
        pip_install_if_nedd(package)


# 判断服务是否启动，启动则杀掉进程
def kill_web_app_if_exists():
    with cd('/tmp'):
        # 判断是否存在app.pid文件，如果存在，说明应用已经运行，读取app.pid中的进程ip，通过kill关闭进程
        if exists('app.pid'):
            pid = run('cat app.pid')
            print(yellow("kill app which pid is {0}".format(pid)))
            with settings(hide("everything"), warn_only=True):
                run("kill -9 {0}".format(pid))
        # 如果不存在此文件，说明服务未运行
        else:
            print(red("pid file not exists"))


# 上传flask文件
def upload_web_app():
    put('app.py', '/tmp/app.py')


# 运行flask app应用
def run_web_app():
    with cd('tmp'):
        run('gunicron -w 1 app:app -b 0.0.0.0:5000 -D -p /tmp/app.pid --log-file=/tmp/app.log', pty=False)


# 重启服务，包含之前定义的启动函数
def restart_web_app():
    kill_web_app_if_exists()
    run_web_app()


# 根据web的role部署
@task
@roles('web')
def deploy_web():
    install_package()
    upload_web_app()
    restart_web_app()


# 封装总的任务列表
@task
def deploy_all():
    execute(deploy_db)
    execute(deploy_web)











