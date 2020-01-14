# 先将敏感词文件读取到List中存储
with open("filtered_words.txt", "r", encoding="UTF-8") as f:
    data = f.read().splitlines()
    print(data)

# 判断输入的词是否在这个列表中
a = str(input("请输入文字："))
if a in data:
    print("Freedom")
else:
    print("Human Rights")


