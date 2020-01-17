"""
根据ini格式的配置文件base.cfg，也就是主机信息的文件
待上层的基础服务（例如nginx）安装完成
根据模板文件渲染动态生成配置文件
"""
import os
import jinja2
import configparser


NAMES = ["issa_server_a_host", "issa_server_a_port",
         "issa_server_b_host", "issa_server_b_port",
         "issa_server_c_host", "issa_server_c_port"]


def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path)).get_template(filename).render(**kwargs)


def parser_vars_into_globals(filename):
    parser = configparser.ConfigParser()
    parser.read(filename)
    for name in NAMES:
        # globals() 函数会以字典类型返回当前位置的全部全局变量。
        # 将配置文件中的主机Ip信息和端口，加入到全局变量中
        globals()[name] = parser.get('DEFAULT', name)


def main():
    parser_vars_into_globals('base.cfg')
    with open('pass_service1.xml', 'w') as f:
        f.write(render('pass_service1_template.xml', **globals()))
    with open('pass_service2.xml', 'w') as f:
        f.write(render('pass_service2_template.xml', **globals()))


if __name__ == '__main__':
    main()
