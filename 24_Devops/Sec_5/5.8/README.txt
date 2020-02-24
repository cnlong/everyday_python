部署mondodb的案例
1.解压mondb的安装包到mongo目录
2.创建mongodata目录用于保存MongoDB的数据库文件
3.mongodb数据库启动的命令:mongo/bin/mongod --fork --logpath mongodata/mongod.log --dbpath mongodata