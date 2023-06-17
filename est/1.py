from functools import reduce

def solution(histogram):
    answer = 0
    r = len(histogram)
    c = len(histogram[0])

    cols = [[] for i in range(c)]
    for _c in range(c):
        for _r in range(r-1,-1,-1):
            cols[_c].append(str(histogram[_r][_c]))

    res = []

    for col in cols:
        strcol = ''.join(col)
        idx_0 = strcol.rfind('0')
        idx_1 = strcol.rfind('1')
        idx_2 = strcol.rfind('2')

        if idx_2 == -1:
            res.append(1)

        elif idx_1 > idx_2 or '0' in strcol[0:idx_2]:
            res.append(1)

        else:
            res.append((idx_2+1)-idx_1)

    answer = reduce(lambda x, y: x * y, res)
    
    return answer

print(solution([[0,0,0,0,0,0,1], [0,0,0,1,0,0,1], [0,1,0,1,0,0,1],
                [1,1,2,2,1,0,1], [2,2,2,2,1,2,2], [2,2,1,1,1,2,2], [2,2,1,1,1,2,2]]))

print(solution([[0,0,0,0,0], [0,0,0,0,0], [2,2,0,0,0],
                [1,0,1,0,0], [2,1,2,2,2], [2,1,2,2,2]]))
