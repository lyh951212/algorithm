from collections import deque
import numpy as np
import heapq

def solution(queue):
    answer = []
    h= []
    myq = deque()
    h.append((0, queue, [0,0,0]))

    q = deque(queue)
    while h:
        (s, numbers, cost) = heapq.heappop(h)
        
        if numbers.count(1) + cost[0] == numbers.count(2) + cost[1] == numbers.count(3) + cost[2]:
            answer = list(cost)
            break

        ar_1 = np.add(cost, [1,0,0])
        ar_2 = np.add(cost, [0,1,0])
        ar_3 = np.add(cost, [0,0,1])
        heapq.heappush(h, (sum(ar_1), numbers[1:], list(map(int, ar_1)) ))
        heapq.heappush(h, (sum(ar_2), numbers[1:], list(map(int, ar_2)) ))
        heapq.heappush(h, (sum(ar_3), numbers[1:], list(map(int, ar_3)) ))
        
        # myq.append((numbers[1:], list(map(int, np.add(cost, [1,0,0]))) ))
        # myq.append((numbers[1:], list(map(int, np.add(cost, [0,1,0]))) ))
        # myq.append((numbers[1:], list(map(int, np.add(cost, [0,0,1]))) ))
        
    
    return answer

print(solution([2,1,3,1,2,1]))
print(solution([3,3,3,3,3,3]))
print(solution([1,2,3]))