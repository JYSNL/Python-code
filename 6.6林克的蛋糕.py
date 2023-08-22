n_f=input('输入蛋糕的数量与朋友的数量 空格隔开：').split(' ')
number_cake=int(n_f[0])        #蛋糕的数量
friend=int(n_f[1])
people = friend+1        #分蛋糕的人
R=[]                  #每个蛋糕的半径
cakess=input('输入每个蛋糕的半径  空格隔开').split(' ')
for i in range(0,number_cake):
    R.append(int(cakess[i]))
#print(cake)
                            #当蛋糕数多于人时
if number_cake>people:
    R.sort(reverse=True)
    r=R[people-1]
    per=3.1415926*r**2
    print('%.6f'%per)
                            #当蛋糕数等于人数
