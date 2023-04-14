import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    result = deque()
    for i in range(n):
        result.append(int(input()))

    numbers = deque([i+1 for i in range(n)])
    q = deque()
    
    ans = []
    while result:
        if q and result[0] == q[-1]:
            ans.append("-")
            result.popleft()
            q.pop()

        elif len(q) == 0  or result[0] != q[-1]:
            ans.append("+")
            if numbers:
                q.append(numbers.popleft())
            else:
                print("NO")
                sys.exit()
                

    for a in ans:
        print(a)

