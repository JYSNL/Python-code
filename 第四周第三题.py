print("由行列输入的矩阵如下:(请按提示输入)")
a = int(input("输入行："))
b = int(input("输入列："))
arr = input("输入矩阵元素").split(' ')
for i in range(0, len(arr)):
        x = int(arr[i])
        print('%3d' % x, end=' ')
        if (i+1) % b == 0:
            print('\n')
print('\n')


print("自动生成矩阵:")
c = int(input("输入行："))
d = int(input("输入列："))
for i in range(1, c+1):
    for j in range(1, d+1):
        x = i*j
        print('%5d' % x, end=' ')
    print('\n')
