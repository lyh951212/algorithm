from collections import deque

# AAG CGA는 set으로 diff하면 하나만 다르지만
# 각 자리수의 문자가 모두 다르다. 
def isOneDifferent(start, end):
    cmp = 0
    for i, s in enumerate(start):
        if s != end[i]:
            cmp+=1

    return False if cmp > 1 else True

def solution(begin, target, words):
    answer = 0
    
    visited = dict()
    d = dict()
    q = deque()
    
    if target not in words:
        return 0
    
    for i, iword in enumerate(words):
        d[iword] = list()
        visited[iword] = False
        
        if isOneDifferent(begin, iword) == True:
            q.append((iword, 1))
            
        for j, jword in enumerate(words):
            if i==j:
                continue
                
            if isOneDifferent(iword, jword) == True:
                d[iword].append(jword)
            
    while q:
        (w , time) = q.popleft()
        #print(w, time)
        if w == target:
            answer = time
            break
                
        visited[w] = True
        nextwords = d.get(w)
        if nextwords:
            for nw in nextwords:
                if visited.get(nw) == False:
                    q.append((nw, time+1))
        
        
    return answer


print(solution("GAA", "AFA", ["AAG", "AFA"]))