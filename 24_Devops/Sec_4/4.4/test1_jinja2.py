import jinja2
import os


def render(tpl_path, **kwargs):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(loader=jinja2.FileSystemLoader(path)).get_template(filename).render(**kwargs)


def test_template():
    title = "Titile  H    "
    items = [{'href': 'a.com' ,'caption': 'ACaption'}, {'href': 'b.com', 'caption': 'Bcaption'}]
    content = "This is content"
    # locals() 函数会以字典类型返回当前位置的全部局部变量
    result = render('simple.html', **locals())
    print(result)

def test_extend():
    result = render('index.html')
    print(result)

if __name__ == '__main__':
    # test_template()
    # test_extend()
    links = [{'title': '杭州地铁三期规划正式获批 3号线即将上马', 'href': 'http://zzhz.zjol.com.cn/system/2016/12/21/021404496.shtml'},
             {'title': '涉及房地产的四个关键点', 'href': 'http://zzhz.zjol.com.cn/system/2016/12/19/021402558.shtml'},
             {'title': '丁建刚特别评论：“长效机制”路漫长需法治', 'href': 'http://zzhz.zjol.com.cn/system/2016/12/15/021399903.shtml'}]
    content = render('hzfc.html', items=links)
    print(content)