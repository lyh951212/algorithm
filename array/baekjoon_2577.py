
## 브론즈 5
## 31256kb	40ms

import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

numtostr = list(map(str, str(A*B*C)))

result = [ 0 for i in range(10)]
for s in numtostr:
    result[int(s)] += 1

for i in result:
    print(i)