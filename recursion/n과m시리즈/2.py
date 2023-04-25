import sys

def recursion(idx, cur):
    global arr, n, m

    if len(cur) == m:
        print(*cur)
        return 
    
    for i in range(idx, len(arr)):
        if arr[i] in cur:
            continue
        
        cur.append(arr[i])
        recursion(i+1, cur)
        cur.pop()


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split(" "))
    arr = [i+1 for i in range(n)]
    recursion(0, [])