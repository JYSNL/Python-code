all=int(input(''))
def power(base,exponent):
    res = 1
    while exponent:
        if exponent & 1:  # 判断当前的最后一位是否为1，如果为1的话，就需要把之前的幂乘到结果中。
            res *= base
        base *= base  # 一直累乘，如果最后一位不是1的话，就不用了把这个值乘到结果中，但是还是要乘。
        exponent = exponent >> 1
    return res

for i in range(1,all+1):
    array=input('').split(' ')
    a=int(array[0])
    b=int(array[1])
    p=int(array[2])
    '''for j in range(1,b+1):
        s=s*a'''
    s=power(a,b)
    print(s%p)