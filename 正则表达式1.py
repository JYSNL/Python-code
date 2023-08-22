import re

pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.match(pattern,string,re.I)
print(match)
string = '项目名称MR_SHOP mr_shop'
match = re.match(pattern,string,re.I)
print(match)

print('---------------------------------')

pattern = r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
str1 = '127.0.0.1 138.23.65.99'
match = re.findall(pattern,str1)
for i in match:
    print(i[0])

print('---------------------------------')

pattern = r'1[34578]\d{9}'
string = '中奖号码为:845698 联系电话为:13611111111'
change = '1xxxxxxxxxx'
result = re.sub(pattern,change,string)
print(result)

print('---------------------------------')

pattern = r'[&|?]'
url = 'http://www.mingrisoft.com/login.jsp?username="mr"&pwd="mrsoft"'
result = re.split(pattern,url)
print(result)