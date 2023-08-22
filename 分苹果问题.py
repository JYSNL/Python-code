'''
先输入总的测试数据次数
第一个数为苹果数 第二个数为篮子数   输出总的放法   篮子均相同
'''
def putapples(m,n):
    if m == 1 or m == 0 or n == 1:
        return 1
    if m < 0:
        return 0
    return putapples(m - n, n) + putapples(m, n - 1)



turns=int(input(''))

for i in range(1,turns+1):

    a=input('').split(' ')

    apples=int(a[0])
    baskets=int(a[1])

    works=putapples(apples,baskets)
    print('{0}'.format(works))


