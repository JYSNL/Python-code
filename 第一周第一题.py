sentence = input("输入字符串:")
place = int(input("输入位置:"))
new_sen = ""
for i in range(0,len(sentence)):
    if i!=place-1:
        new_sen = new_sen + sentence[i]

print("删除后的字符串：" + new_sen)

