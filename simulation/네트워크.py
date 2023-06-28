from collections import deque

def solution(n, computers):
    answer = 0
    d = dict()
    for i, c in enumerate(computers):
        d[i] = list()
        for j, _c in enumerate(c):
            if i != j and _c == 1:
                d[i].append(j)
                
    print(d)
    visited = [False for i in range(n)]
    q = deque()
    for i in range(n):
        if visited[i]==False:
            q.append(i)
            answer+=1
            while q:
                key = q.popleft()
                v = d.get(key)
                
                while v:
                    last = v[-1]
                    if visited[last] == False:
                        q.append(last)
                    v.pop()
                    visited[last] = True
                    
    return answer