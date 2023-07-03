from collections import deque

def solution(maps):
    answer = -1
    R = len(maps)
    C = len(maps[0])
    
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    
    start = (0,0)
    end = (R-1, C-1)
    visited = [[False for i in range(C)] for j in range(R)]
    visited[0][0] = True
    
    q = deque()
    q.append((start, 1))
    
    while q:
        (pos, time) = q.popleft()
        
        if pos == end:
            answer = time
            break
                    
        for i in range(4):
            _dr = pos[0]+dr[i]
            _dc = pos[1]+dc[i]
            if 0<= _dr < R and 0 <= _dc < C and visited[_dr][_dc] == False and maps[_dr][_dc] == 1:
                q.append(((_dr, _dc), time+1))
                visited[_dr][_dc] = True
            
    
    return answer