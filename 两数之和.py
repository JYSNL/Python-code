target_2=input('').split(' ')
target = int(target_2[0])
numbers = int(target_2[1])
a=[]
s2=input('').split()
for k in range(numbers):
    a.append(int(s2[k]))
a=sorted(a)
n1=0
n2=len(a)-1
while n1<len(a)-1:
    if n1<n2:
        if a[n1]+a[n2] == target:
            print(n1,n2)
            n1+=1
            n2-=1
            while a[n1-1]==a[n1]:
                n1+=1
            while a[n2+1]==a[n2]:
                n2-=1
        elif a[n1]+a[n2] > target:
            n2-=1
            while a[n2+1]==a[n2]:
                n2-=1
        else:
            n1+=1
            while a[n1-1]==a[n1]:
                n1+=1
            n2=len(a)-1
    else:
        break