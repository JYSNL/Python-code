n=int(input(''))
u=input('').split(' ')
number=[]
for i in range(0,n):
    number.append(int(u[i]))
number.sort(reverse=False)
gentle=int(input(''))
a1,a2=0,n-1
while a1<a2:
    s=number[a1]+number[a2]
    if s<gentle:
        a1+=1
    elif s>gentle:
        a2-=1
    else:
        print(number[a1],number[a2],end=' ')
        break
if a1==a2:
    print('No')