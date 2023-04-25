import sys
from collections import deque

def bfs(search_pos):
    global arr
    global r,c, is_visited

    q = deque()
    for pos in search_pos:
        (x,y) = pos
        q.append((x,y))
        is_visited[x][y] = True
    
    
    cnt = 0
    melting = [] 
    while q:
        (_r, _c) = q.popleft()

        for i in range(4):
            _dr = _r + dr[i]
            _dc = _c + dc[i]

            if 0 <= _dr < r and 0 <= _dc < c and is_visited[_dr][_dc] == False:
                if arr[_dr][_dc] == 1:
                    cnt+=1
                    arr[_r][_c] = 0
                    melting.append((_dr, _dc))
                    is_visited[_dr][_dc]= True
                else:
                    q.append((_dr, _dc))
                    is_visited[_dr][_dc] = True

    for w in melting:
        (a, b) = w
        arr[a][b] = 0

    return melting

if __name__ == "__main__":
    input = sys.stdin.readline
    r, c = map(int, input().split(" "))
    arr = [ list(map(int, input().split(" "))) for i in range(r)]

    is_visited = [ [False for j in range(c)] for i in range(r)]

    # 상 하 좌 우 
    dr = [-1, 1, 0, 0] 
    dc = [0, 0, -1, 1] 

    start_pos = [[0,0]]
    time = 0
    res = []
    while start_pos:
        start_pos = bfs(start_pos)
        res.append(start_pos)
        time += 1


    print(time-1)
    print(len(res[-2]))

