import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()

    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        (x,y,crash) = q.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if x == N - 1 and y == M - 1:
            return visited[crash][x][y]
        
        for i in range(4):
            _dr = x + dr[i]
            _dc = y + dc[i]

            if 0 <= _dr < N and 0<= _dc< M and visited[crash][_dr][_dc] == -1:
                if arr[_dr][_dc] == 1:
                    if crash < 1:
                        q.append((_dr, _dc, crash+1))
                        visited[crash+1][_dr][_dc] = visited[crash][x][y] + 1
                else:
                    q.append((_dr, _dc, crash))
                    visited[crash][_dr][_dc] = visited[crash][x][y] + 1

    return -1
                


dc = [1,-1, 0, 0]
dr = [0,0, 1, -1]
N, M = map(int, input().split(" "))
arr = []
for n in range(N):
    arr.append(list(map(int, input().rstrip())))

visited = [[[ -1 for i in range(M)] for j in range(N)] for k in range(2)]

print(bfs())