import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

stack = []
stack.append(n-1)
res = [0] * n

for i in range(n-2, -1, -1):
    while stack and arr[stack[-1]] < arr[i]:
        res[i] += 1
        res[i] += res[stack[-1]]
        stack.pop()

    stack.append(i)

print(sum(res))