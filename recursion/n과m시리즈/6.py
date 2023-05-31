import sys

def recursion(start, cur):
    global arr, n, m

    if len(cur) == m:
        print(*cur)
        return 
    
    for i in range(start, len(arr)):
        if arr[i] in cur:
            continue

        cur.append(arr[i])
        recursion(i+1, cur)
        cur.pop()


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    arr.sort()
    recursion(0, [])