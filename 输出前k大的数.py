n=int(input(''))
a=input('').split(' ')
c=[]
for i in range(0,n):
    c.append(int(a[i]))
c.sort(reverse=True)
k=int(input(''))
for i in range(0,k):
    print(c[i])