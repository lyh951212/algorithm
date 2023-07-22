import sys
input = sys.stdin.readline
n = int(input())

def solution(strlist):
    open = []
    for i, ch in enumerate(strlist):
        if ch == "(":
            open.append(i)
        else:
            if len(open) == 0:
                return "NO"
            open.pop()

    if len(open) > 0:
        return "NO"
    return "YES"

res = []
for i in range(n):
    strlist = list(map(str, input().rstrip()))
    res.append(solution(strlist))

for r in res:
    print(r)
