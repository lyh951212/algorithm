import sys
input = sys.stdin.readline

arr = list(map(str, input().rstrip()))

open_stack = []
result = 0

for i , s in enumerate(arr):
    if s == ")":
        if arr[i-1] == "(":
            ## 레이저임
            open_stack.pop()
            result += len(open_stack)
        else:
            ## 쇠막대기임
            open_stack.pop()
            result += 1

    else:
        open_stack.append(i)

print(result)
