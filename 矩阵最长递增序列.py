def solve( matrix):
    dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    maxLen = 0

    def rr(i, j):
        # 若从当前位置出发的路径已经搜索过，直接返回
        # 否则从当前位置出发搜索再返回
        if dp[i][j] == 0:
            up = rr(i - 1, j) if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j] else 0
            down = rr(i + 1, j) if i + 1 <= len(matrix) - 1 and matrix[i][j] < matrix[i + 1][j] else 0
            left = rr(i, j - 1) if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1] else 0
            right = rr(i, j + 1) if j + 1 <= len(matrix[0]) - 1 and matrix[i][j] < matrix[i][j + 1] else 0
            dp[i][j] = max(up, down, left, right) + 1
        return dp[i][j]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            maxLen = max(rr(i, j), maxLen)
    return maxLen



x = input().split(' ')
a = int(x[0])
b = int(x[1])
A = []
for i in range(a):
    yy = input().split(' ')
    if yy[-1] == '':
        yy.pop()
    A.append(yy)
print(A)
answer = solve(A)
print(answer)