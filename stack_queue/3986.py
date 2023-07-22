import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
# 현재 값과 이전에 있던 stack[-1]과 비교해서 
# 같으면 pop() 다르면 s[i]를 추가하는 방법
# 괄호 열고 닫기 문제와 비슷

for _ in range(n):
    s = input().rstrip()
    stack = []

    for i in range(len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])

    if not stack:
        cnt += 1
print(cnt)