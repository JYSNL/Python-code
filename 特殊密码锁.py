pwd_1=input('')
pwd_2=input('')
pwd_11=list(pwd_1)
pwd_22=list(pwd_2)
pwd_3=[]
pwd_4=[]
for i in range(len(pwd_11)):
    pwd_3.append(int(pwd_11[i]))
for i in range(len(pwd_22)):
    pwd_4.append(int(pwd_22[i]))  #已经得到两个数字列表
#print(pwd_3)
#print(pwd_4)
summary=0
def change(pwd1,pwd2,n):
    if n==0:
        if n+2<len(pwd1):
            if pwd1[n+2]==pwd2[n+2]:
                if pwd1[n]==0:
                    pwd1[n]=1
                    if n+1<len(pwd_1):
                        if pwd1[n+1]==0:
                            pwd1[n+1]=1
                        else:
                            pwd1[n+1]=0
                else:
                    pwd1[n]=0
                    if n+1<len(pwd_1):
                        if pwd1[n+1]==0:
                            pwd1[n+1]=1
                        else:
                            pwd1[n+1]=0
            else:
                change2(pwd1,pwd2,n)
    elif n==len(pwd1)-1:
        print('impossible')
    else:
        if pwd1[n]==0:
            pwd1[n]=1
            if n+1<len(pwd_1):
                if pwd1[n+1]==0:
                    pwd1[n+1]=1
                    if n+2<len(pwd1):
                        if pwd1[n+2]==0:
                            pwd1[n+2]=1
                        else:
                            pwd1[n+2]=0
                else:
                    pwd1[n+1]=0
                    if n+2<len(pwd1):
                        if pwd1[n+2]==0:
                            pwd1[n+2]=1
                        else:
                            pwd1[n+2]=0
        else:
            pwd1[n]=0
            if n+1<len(pwd_1):
                if pwd1[n+1]==0:
                    pwd1[n+1]=1
                    if n+2<len(pwd1):
                        if pwd1[n+2]==0:
                            pwd1[n+2]=1
                        else:
                            pwd1[n+2]=0
                else:
                    pwd1[n+1]=0
                    if n+2<len(pwd1):
                        if pwd1[n+2]==0:
                            pwd1[n+2]=1
                        else:
                            pwd1[n+2]=0
def change2(pwd1,pwd2,d):
    if pwd1[d]==0:
        pwd1[d]=1
    else:
        pwd1[d]=0
    if pwd1[d+1]==1:
        pwd1[d+1]=0
    else:
        pwd1[d+1]=1
    if pwd1[d+2]==0:
        pwd1[d+2]=1
    else:
        pwd1[d+2]=0
for i in range(len(pwd_3)):
    if pwd_3[i]==pwd_4[i]:
        continue
    else:
        change(pwd_3,pwd_4,i)
        summary+=1
#print('---------------')
#print(pwd_3)
#print(pwd_4)
if pwd_3==pwd_4:
    print(summary)