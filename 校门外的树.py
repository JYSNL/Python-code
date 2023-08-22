t_m=input('').split(' ')
total=int(t_m[0])
move=int(t_m[1])
trees=[]

target=0
for i in range(0,total+1):
    trees.append(int('1'))
for j in range(0,move):
    move2=input('').split(' ')
    start=int(move2[0])
    stop=int(move2[1])
    for k in range(start-1,stop):
        trees[k]=0
for s in range(0,total+1):
    if trees[s]!=0:
        target+=1
print(target)
