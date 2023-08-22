'''def square_root_1(k):
    c = k
    g = c/2
    i = 0
    while abs(g**3 - c) > 0.00000000001:
        g = (2*g)/3 + c/(3*(g**2)) #此为开三次方根的公式
        i = i + 1
    print("% .6f" % (g))
k = float(input(''))
square_root_1(k)'''
from math import fabs, copysign     #导入一个库

x = float(input(''))          #输入一个浮点数
y = copysign(fabs(x) ** (1 / 3), x)         #公式 分母分子均可改
print('%.6f'%y) #输出