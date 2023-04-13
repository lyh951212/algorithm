import sys
sys.setrecursionlimit(10 ** 9)

# dfs 탐색
def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    
    dp[x][y] = 0

    for i in range(4):
        _dr = x + dx[i]
        _dc = y + dy[i]

        if 0 <= _dr < m and 0<= _dc <n and graph[x][y] > graph[_dr][_dc]:
            if dp[_dr][_dc] == -1:
                dp[x][y] += dfs(_dr, _dc)
            else:
                dp[x][y] += dp[_dr][_dc] 

    return dp[x][y]


m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
print(dfs(0, 0))