import sys

def recursion(cur):
    global arr, n, m

    if len(cur) == m:
        print(*cur)
        return 
    
    for i in range(len(arr)):
        cur.append(arr[i])
        recursion(cur)
        cur.pop()


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    arr.sort()
    recursion( [])