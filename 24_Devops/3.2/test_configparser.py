import  configparser



cf = configparser.ConfigParser(allow_no_value=True)
cf.read('mysql.cnf')
print(cf.sections())
print(cf.has_section('client'))
print(cf.options('client'))
print(cf.options('mysqld'))
print(cf.has_option('client', 'user'))
print(cf.get('client', 'host'))
print(cf.get('mysqld', 'skip-external-locking'))
print(type(cf.get('client', 'port')))
print(type(cf.getint('client', 'port')))

cf.remove_section('client')
cf.add_section('mysql')
cf.set('mysql', 'host', '127.0.0.1')
# 选项的值必须是字符串
cf.set('mysql', 'port', '3306')
cf.write(open('my_copy.cnf', 'w'))
