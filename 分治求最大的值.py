def get_max(numList):
    return max(numList)    #使用了max函数返回列表中最大值
def solution(numList):
    n = len(numList)
    if n<2:
        return get_max(numList)
    temp_list = [numList[i:i+2] for i in range(0,n,2)]
    print('^^^^****^^^^')
    print(temp_list)
    max_list = list(map(get_max,temp_list))
    print(max_list)
    if len(max_list) == 1:
        return max_list[0]
    else:
        return solution(max_list)
a=input('').split(' ')
b=[]
for i in range(0,len(a)):
   b.append(int(a[i]))
print(solution(b))