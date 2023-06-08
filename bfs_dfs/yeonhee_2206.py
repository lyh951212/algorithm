import sys
from collections import deque
input = sys.stdin.readline
# 279432kb,	1604ms
def bfs():
    queue = deque()
    queue.append((0,0,0,1))
    visited[0][0][0] = True
    visited[0][0][1] = True

    while queue:
        _r, _c, wall, cnt = queue.popleft()
        if _r == n-1 and _c == m-1:
            return cnt
        
        for i in range(4):
            _dr = _r + dr[i]
            _dc = _c + dc[i]

            if 0<=_dr<n and 0<=_dc<m:
                if graph[_dr][_dc] == 0:
                    if visited[_dr][_dc][wall] == False:
                        queue.append((_dr,_dc,wall,cnt+1))
                        visited[_dr][_dc][wall] = True
                else:
                    if wall<1 and visited[_dr][_dc][wall] == False:
                        queue.append((_dr,_dc,wall+1,cnt+1))
                        visited[_dr][_dc][wall] = True
    
    return -1

if __name__ == "__main__":
    n,m = map(int, input().split(" "))
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().rstrip())))

    # 오 왼 위 아래
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    visited = [[[False for _ in range(2)]  for j in range(m)] for i in range(n)]
    print(bfs())