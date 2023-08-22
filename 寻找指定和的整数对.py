n=int(input(''))
u=input('').split(' ')
number=[]
first=[]
second=[]
for i in range(0,n):
    number.append(int(u[i]))
gentle=int(input(''))
for j in range(0,n-1):
    a1=number[j]
    remain=gentle-a1
    for k in range(j+1,n):
        a2=number[k]
        if a2==remain:
            if a1>a2:
                first.append(a2)
                second.append(a1)
            else:
                first.append(a1)
                second.append(a2)
a=0
if first:
    for item1 in range(a,len(first)-1):
        if first[a]<=first[a+1]:
            continue
        else:
            a=a+1
    print(first[a],second[a],end=' ')
else:
    print('No')