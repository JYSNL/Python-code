N_q = input('').split(' ')
N = int(N_q[0])
q = int(N_q[1])
n = input('').split(' ')
monsters = []
for i in range(0, N):
    monsters.append(int(n[i]))
k = []
for i in range(0, q):
    monster = int(input(''))
    k.append(monster)
for j in range(0, q):
    game = k[j]
    b = [-1, -1]
    for i in range(0, N):
        if monsters[i] < game:
            continue
        elif monsters[i] == game and b[0] == -1:
            b = [i, i]
        elif monsters[i] == game and b[0] != -1:
            b[1] = i
        else:
            break
    for i in range(0, 2):
        print(b[i], end = ' ')
    print()
