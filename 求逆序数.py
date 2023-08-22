n = int(input(''))
s = input('').split(' ')
c = []
total = 0
for i in range(0, len(s)):
    c.append(int(s[i]))
for i in range(0, len(c)-1):
    for j in range(i+1, len(c)):
        if c[i] > c[j]:
            total += 1
print(total)
