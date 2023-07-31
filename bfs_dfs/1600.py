import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split(" "))

arr = []
for i in range(H):
    arr.append(list(map(int, input().split(" "))))

vis = [[[ -1 for j in range(W)] for i in range(H)] for h in range(K+1)] 

q = deque()
q.append((0,0,0))
vis[0][0][0] = 0
answer = 0

dr_m = [0 , 0, 1, -1]
dc_m = [1, -1, 0, 0]

dr_h = [-1, -2, 1, 2, -1, -2, 1, 2]
dc_h = [2, 1, 2, 1, -2, -1, -2, -1]

while q:
    (x,y,h) = q.popleft()

    if x == H-1 and y == W-1:
        print(vis[h][x][y])
        sys.exit()
        
    for i in range(4):
        _dx = x + dr_m[i]
        _dy = y + dc_m[i]

        if 0<=_dx<H and 0<=_dy<W and vis[h][_dx][_dy] == -1 and arr[_dx][_dy] == 0:
            vis[h][_dx][_dy] = vis[h][x][y]+1
            q.append((_dx, _dy, h))

    if h < K:
        for i in range(8):
            _dx = x + dr_h[i]
            _dy = y + dc_h[i]

            if 0<=_dx<H and 0<=_dy<W and vis[h+1][_dx][_dy] == -1 and arr[_dx][_dy] == 0:
                vis[h+1][_dx][_dy] = vis[h][x][y]+1
                q.append((_dx, _dy, h+1))
    
print(-1)