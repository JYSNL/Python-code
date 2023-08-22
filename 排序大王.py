i = input('').split(' ')
b=[]
for j in range(0,len(i)):
    b.append(int(i[j]))
b.sort(reverse=False)
print(b)
print(b[22])
print(b[16])