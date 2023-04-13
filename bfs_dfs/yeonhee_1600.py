import sys
from collections import deque # !!!

input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((0,0,k)) # (row idx, col idx, time) 
    while queue:
        (r,c,z) = queue.popleft() # pop()으로 하면 오답처리 된다. 왜???
        if c == w-1 and r == h-1:
            return visited[r][c][z]
        
        # 원숭이
        for i in range(4):
            dr = r + monkey_dir_r[i]
            dc = c + monkey_dir_c[i]

            if dr < 0 or dr >= h or dc < 0 or dc >= w:
                continue
            
            if visited[dr][dc][z] > 0:
                continue

            if arr[dr][dc] == 1:
                continue

            visited[dr][dc][z] = visited[r][c][z] + 1
            queue.append((dr, dc, z))

        # 말
        if z > 0:
            for i in range(8):
                dr = r + horse_dir_r[i]
                dc = c + horse_dir_c[i]

                if dr < 0 or dr >= h or dc < 0 or dc >= w:
                    continue
                
                if visited[dr][dc][z-1] > 0:
                    continue

                if arr[dr][dc] == 1:
                    continue

                visited[dr][dc][z - 1] = visited[r][c][z] + 1
                queue.append((dr, dc, z-1))
            
    return -1


if "__main__" == __name__:
    k = int(input())
    w,h = map(int, input().split(" "))
    arr = list()
    for i in range(h):
        arr.append(list(map(int, input().split(" "))))

    # 3차원 배열 k는 30이하의 정수
    visited = [[[0 for i in range(31)] for i in range(w)] for j in range(h)]

    # 동 서 남 북
    monkey_dir_r = [0, 0, 1 , -1]
    monkey_dir_c = [1, -1, 0, 0]

    # 오위  오아래  왼위    왼아래
    horse_dir_r = [-2, -1, 2, 1, -1, -1, 2, 1]
    horse_dir_c = [1, 2, 1, 2, -1, -2, -1, -2]
    print(bfs())


