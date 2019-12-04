import requests


url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9125"
s = requests.session()
res = s.get(url)
c = requests.cookies.RequestsCookieJar()
c.set('cookie-name','cookie-value')
s.cookies.update(c)
print(s.cookies.get_dict())