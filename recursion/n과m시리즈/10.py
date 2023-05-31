import sys
import copy

def recursion(idx, cur):
    global arr, n, m, ans, visited

    if len(cur) == m:
        ans.add(tuple(copy.deepcopy(cur)))
        return 
    
    for i in range(idx, len(arr)):
        if visited[i]:
            continue

        cur.append(arr[i])
        visited[i] = True
        recursion(i+1, cur)
        visited[i] = False
        cur.pop()


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split(" "))
    arr = sorted(list(map(int, input().split(" "))))
    visited = [False]*n

    ans = set()
    recursion(0, [])
    for a in sorted(ans):
        print(*a)
