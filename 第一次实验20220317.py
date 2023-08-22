import re
file = open(r"E:\C课程\大二下\python程序设计\数据1.txt", "r", encoding="utf-8")
text = file.read()
file.close()
pattern1 = r'([\u4e00-\u9fa5 ]*)(\u53a6\u95e8)([\u4e00-\u9fa5 ]*)'
mess = re.search(pattern1,text)
print(mess.group())
pattern2 = r"([\u4e00-\u9fa5 ]+[：:](\d*-\d*|\d{7,}([,， ]*\d*)*))"
items = re.findall(pattern2,text)
for item in items:
        print(''.join(item[0].split()))