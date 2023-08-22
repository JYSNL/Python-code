a = input('')
b = a.split(' ')
target = int(b[0])
numbers = int(b[1])
s1 = input('')
s2 = s1.split(' ')
s3=[]
for k in range(len(s2)):
    s3.append(int(s2[k]))
s3=sorted(s3)
#print(s3)
for n1 in range(len(s3)):
    for n2 in range(n1+1,len(s3)):
        for n3 in range(n2+1,len(s3)):
            for n4 in range(n3+1,len(s3)):
                if s3[n1]+s3[n2]+s3[n3]+s3[n4]==target:
                    if s3[n1]!=s3[n2]!=s3[n3]!=s3[n4]:
                        print(str(s3[n1])+' '+str(s3[n2])+' '+str(s3[n3])+' '+str(s3[n4]))