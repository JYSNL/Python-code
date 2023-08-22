def dfs(idx):
    global ans
    if len(bus) >= ans:
        return
    if idx >= N:
        ans = len(bus)
        return
    for i in range(len(bus)):
        if bus[i] + C[idx] <= W:
            bus[i] += C[idx]
            dfs(idx + 1)
            bus[i] -= C[idx]
    bus.append(C[idx])
    dfs(idx + 1)
    bus.pop()

N, W = map(int, input().split())
C = []
for _ in range(N):
    C.append(int(input()))
C.sort(reverse=True)
bus = []
bus.append(C[0])
ans = N
dfs(1)
print(ans)
