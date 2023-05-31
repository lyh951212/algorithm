import sys
input = sys.stdin.readline

size = int(input())
arr = list(map(int, input().split(" ")))
x = int(input())
cnt = 0
for i in range(size-1):
    for j in range(i+1, size):
        if arr[i] + arr[j] == x:
            cnt+=1


print(cnt)