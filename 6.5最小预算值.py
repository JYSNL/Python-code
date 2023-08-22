N_M = input('').split(' ')
N = int(N_M[0])
M = int(N_M[1])
M_N = []
for i in range(0, N):
    xn = int(input(''))
    M_N.append(xn)
M_N.sort(reverse=False)
print(M_N)   #
budget = []
for i in range(0,M):
    print(len(M_N))        #
    if len(M_N)>2:
        budget.append(M_N[0]+M_N[len(M_N)-1])
        M_N.pop(0)
        M_N.pop()
        print(M_N)            #
budgets=0
print(budget)            #
for i in range(0,len(budget)):
    if budget[i]>budgets:
        budgets=budget[i]
print(budgets)