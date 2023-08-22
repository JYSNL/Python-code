import itertools
list1=input('').split('')
a=[]
b=len(list1)
for item in list1:
    a.append(item)
array = [i for i in a]
pailie = list(itertools.permutations(array))#要list一下，不然它只是一个对象
for x in pailie:
    for y in x:
        print(y,end=' ')
    print()
