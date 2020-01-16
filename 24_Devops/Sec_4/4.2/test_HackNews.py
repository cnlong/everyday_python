import re
import requests


r = requests.get("https://www.anyknew.com/#/")
print(r.content.decode("utf-8"))

pattern = '("https://.*?")'
re_obj = re.compile(pattern)
a = re_obj.findall(r.content.decode("utf-8"))
print(a)