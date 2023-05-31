import sys
import copy

def recursion(cur):
    global arr, n, m, ans, visited

    if len(cur) == m:
        ans.add(tuple(copy.deepcopy(cur)))
        return 
    
    for i in range(len(arr)):
        if visited[i]:
            continue

        cur.append(arr[i])
        visited[i] = True
        recursion(cur)
        visited[i] = False
        cur.pop()


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split(" "))
    arr = sorted(list(map(int, input().split(" "))))
    visited = [False]*n

    ans = set()
    recursion([])
    for a in sorted(ans):
        print(*a)
