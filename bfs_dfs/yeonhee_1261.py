import sys
from collections import deque
from heapq import heappush, heappop

def bfs():
    q = deque()

    q.append((0,0))
    vis[0][0] = 0

    while q:
        (x,y) = q.popleft()
        
        for i in range(4):
            _dx = x + dx[i]
            _dy = y + dy[i]

            if 0<= _dx < r and 0<=_dy<c and vis[_dx][_dy] == -1:
                if arr[_dx][_dy] == 0:
                    q.appendleft((_dx, _dy))
                    vis[_dx][_dy] = vis[x][y]
                else:
                    q.append((_dx, _dy))
                    vis[_dx][_dy] = vis[x][y] + 1

    return vis[r-1][c-1]

def dijkstra():
    heap = []
    heappush(heap, [0, 0, 0])
    vis[0][0] = 0

    while heap:
        d, x, y = heappop(heap)

        if x == r-1 and y == c-1:
            return d

        for i in range(4):
            _dx = x + dx[i]
            _dy = y + dy[i]

            if 0<= _dx < r and 0<=_dy<c and vis[_dx][_dy] == -1:
                if arr[_dx][_dy] == 0:
                    heappush(heap, [d, _dx, _dy])
                    vis[_dx][_dy] = vis[x][y]
                else:
                    heappush(heap, [d+1, _dx, _dy])
                    vis[_dx][_dy] = vis[x][y] + 1

    return vis[r-1][c-1]


if __name__ == "__main__":
    input = sys.stdin.readline
    c,r = map(int, input().split(" "))
    arr = []
    for _ in range(r):
        arr.append(list(map(int, input().rstrip())))

    vis = [[ -1 for j in range(c)] for i in range(r)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    print(bfs())
    print(dijkstra())