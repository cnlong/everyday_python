"""
使用setuptools打包源码
"""
from setuptools import setup

setup(
    name='longmail',
    version='0.2',
    author='chen long',
    author_email='271138425@qq.com',
    description='A email client in terminal',
    install_requires=['zmail'],
    packages=['longmail'],
)