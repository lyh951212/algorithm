import sys

def recursion(idx, cur):
    global arr, n, m

    if len(cur) == m:
        print(*cur)
        return 
    
    for i in range(idx, len(arr)):
        cur.append(arr[i])
        recursion(i, cur)
        cur.pop()


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split(" "))
    arr = [i+1 for i in range(n)]
    recursion(0, [])