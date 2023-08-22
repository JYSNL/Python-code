b = input('').split(' ')
target = int(b[0])
numbers = int(b[1])
s2 = input('').split(' ')
s=[]
for k in range(len(s2)):
    s.append(int(s2[k]))
s=sorted(s)
#print(s3)
x,y,z=0,1,len(s)-1
while x<len(s)-2:
    if s[x]+s[y]+s[z]==target:
        print(s[x],s[y],s[z])
        if x==len(s)-3:
            break
        else:
            x+=1