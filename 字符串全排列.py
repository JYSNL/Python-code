#字符串任意两个位置字符交换
def str_replace(str, x, y):
  if x == y:
    return str
  x_val = str[x:x+1]
  y_val = str[y:y+1]
  if x < y:
    str = str[0:x] + y_val + str[x+1:y] + x_val + str[y+1:len(str)]
  else:
    str = str[0:y] + x_val + str[y+1:x] + y_val + str[x+1:len(str)]
  return str
#递归求结果
def str_sort(str,x):
  if x == len(str):        #当x为字符串的最大长度时返回当前字符交换的结果
    global str_list
    str_list.append(str)
    return
  for i in range(x,len(str)):
    str = str_replace(str,i,x) #递归遍历第i个字符，
    str_sort(str,x+1)
    str = str_replace(str,x,i) #恢复字符串原来的顺序，便于下次遍历
s = input('')
l=list(s)
l.sort()
s="".join(l)
#print(s)
global str_list
str_list = []
str_sort(s,0)
for item in str_list:
    print(item)