#You may use import as below.
#import math

def solution(n):
    # Write code here.
    answer = 0
    slide = []
    visited = [[0 for j in range(n)] for i in range(n)]
    visited[0][0] = 1
    dir = [(0,1) , (1,0), (0,-1), (-1,0)]
    i = 0
    slide.append(1)
    cur_r = 0
    cur_c = 0
    while len(slide) < n:
        _dr = cur_r+dir[i][0]
        _dc = cur_c + dir[i][1]
        if 0<= _dr < n and 0 <= _dc<n and visited[_dr][_dc] == 0:
            visited[_dr][_dc] = visited[cur_r][cur_c] + 1
            cur_r = _dr
            cur_c = _dc
            if _dr == _dc:
                slide.append(visited[_dr][_dc])
        else:
            i+=1
            i = 0 if i > 3 else i

    answer = sum(slide)
    return answer


#The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret1, ".")
    
n2 = 2
ret2 = solution(n2)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret2, ".")