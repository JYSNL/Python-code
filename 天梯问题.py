#问题：一截天梯 输入总梯子数 每次只能走一步或者两步 求总的走法
def skyfloor(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return skyfloor(n-1)+skyfloor(n-2)

skyfloors=int(input(''))
steps=skyfloor(skyfloors)
print(steps)