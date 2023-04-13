# https://www.acmicpc.net/problem/16401
#  140328kb	3972ms
import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    q.append((r,c,1))
    visited[r][c] = True
    while q:
        (x,y, time) = q.popleft()

        if x == len(graph)-1 and y == len(graph[0])-1:
            return time
        
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]

            if nx not in range(0, len(graph)) or ny not in range(0, len(graph[0])):
                continue

            if visited[nx][ny] == True:
                continue
                
            if graph[nx][ny] == 0:
                continue

            visited[nx][ny] = True
            
            q.append((nx,ny, time+1))
            
    return 0


if "__main__" == __name__:
    n,m = map(int, input().split(" "))
    graph = []
    visited = [[False for i in range(m)] for j in range(n)]
    for _ in range(n):
        graph.append(list(map(int, input().rstrip())))

    # 동 서 남 북
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    print(bfs(0,0))
