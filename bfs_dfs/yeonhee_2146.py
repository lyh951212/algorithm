import sys
from collections import deque

def bfs1(i, j):
    global count
    q = deque()
    q.append((i,j))
    vis[i][j] = True
    arr[i][j] = count
    while q:
        (x, y) = q.popleft()

        for i in range(4):
            _dx = x + dx[i]
            _dy = y + dy[i]

            if 0<=_dx<n and 0<=_dy<n and vis[_dx][_dy] == False and arr[_dx][_dy] != 0:
                vis[_dx][_dy] = True
                arr[_dx][_dy] = count
                q.append((_dx,_dy))


def bfs2(z):
    global answer
    q = deque()

    visited = [[False] * n for _ in range(n)]

    for a in range(n):
        for b in range(n):
            if arr[a][b] == z:
                q.append((a,b))
                # append 와 visited는 짝궁!!!!!!!!
                visited[a][b] = True

    dist = [[0] * n for _ in range(n)]

    while q:
        (a, b) = q.popleft()

        for i in range(4):
            _dx = a + dx[i]
            _dy = b + dy[i]

            if 0<=_dx<n and 0<=_dy<n and visited[_dx][_dy] == False:
                if arr[_dx][_dy] == 0:
                    dist[_dx][_dy] = dist[a][b] + 1
                    q.append((_dx, _dy))
                elif arr[_dx][_dy] != 0 and arr[_dx][_dy] != z:
                    return dist[a][b] # 바로 리턴을 안해주면 시간초과!!!!! bfs이기 때문에 제일 먼저 목표지점에 도착하면 가장 짧은 것임
                    
                visited[_dx][_dy] = True


if __name__ == "__main__":
    input = sys.stdin.readline

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    vis = [[False] * n for _ in range(n)]
    count = 1
    answer = sys.maxsize

    for i in range(n):
        for j in range(n):
            if not vis[i][j] and arr[i][j] == 1:
                bfs1(i, j)
                count += 1

    for i in range(1, count):
        answer = min(answer, bfs2(i))

    print(answer)