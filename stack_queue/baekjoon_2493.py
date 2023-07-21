n = int(input())
towers = list(map(int, input().split()))

stack = []
res = []

for i,n in enumerate(towers):
    while stack and stack[-1][1] < n:
        stack.pop()

    # stack에 무언가 남아있다는 건
    # 마지막에 있는 것이 현재 n보다 크다는 것
    if stack:
        last = stack[-1]
        res.append(last[0])
        stack.append((i+1, n))
    else:
        res.append(0)
        stack.append((i+1 , n))
    
print(" ".join(map(str, res)))