import os
import shutil
import tarfile
import subprocess


def unpackage_mongo(package, package_dir):
    """
    解压安装包的函数
    :param package: 包名
    :param package_dir: 解压到的目录
    :return: 无返回结果
    """
    # 获取安装包除后缀的名称，作为第一次解压的目录
    upackage_dir = os.path.splitext(package)[0]
    # 判断解压目录是否存在，存在，则删除目录
    if os.path.exists(upackage_dir):
        shutil.rmtree(upackage_dir)
    # 判断解压到最终目录是否存在
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    # 解压文件到当前目录
    t = tarfile.open(package, 'r:gz')
    t.extractall('.')
    # 将第一次解压后的目录重命名为指定的目录
    shutil.move(upackage_dir, package_dir)


def execute_cmd(cmd):
    """
    执行命令
    :param cmd: 需要执行的命令
    :return: 返回执行的状态码及执行结果
    """
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return p.returncode, stderr
    return p.returncode, stdout


def main():
    package = 'mongodb-linux-x86_64-debian71-3.4.0.tgz'
    # 获取当前路径全路径
    complete_path = os.path.abspath('.')
    # 获取解压目录全路径
    package_dir = os.path.join(complete_path, 'mongo')
    # 获取数据文件全路径
    data_dir = os.path.join(complete_path, 'mongodata')
    # 获取日志文件全路径
    logfile = os.path.join(complete_path, 'mongod.log')
    if not os.path.exists(package):
        raise SystemExit("{0} not found".format(package))
    if os.path.exists(data_dir):
        shutil.rmtree(data_dir)
    bin_file = os.path.join(package_dir, 'bin', 'mongod')
    cmd = "{0} --fork --dbpath {1} --logpath {2}".format(bin_file, data_dir, logfile)
    unpackage_mongo(package, package_dir)
    os.mkdir(data_dir)
    returncode, out = execute_cmd(cmd)
    if returncode !=0:
        raise SystemExit('execute {0} error: {1}'.format(cmd, out))
    else:
        print("execute {0} successfull".format(cmd))


if __name__ == '__main__':
    main()