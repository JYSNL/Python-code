s = input('')
str1 = list(s)
up, down = 0, 0
for i in str1:
    if i >=  'A'and i <='Z':
        up+=1
    elif i >= 'a' and i <= 'z':
        down+=1
print('大写字母:',up)
print('小写字母:',down)