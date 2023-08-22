a = input().split(' ')
c = [int(a[i]) for i in range(len(a))]
b = tuple(c)
ji = 0
ou = 0
for i in b:
    if i % 2 == 0:
        ou += 1
    else:
        ji += 1
print("奇数共有", ji, "个")
print("偶数共有", ou, "个")
