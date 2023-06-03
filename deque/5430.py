import sys
from collections import deque

input = sys.stdin.readline
result = []
for _ in range(int(input())):
    functions = list(map(str, input().rstrip()))
    arr_size = int(input())
    arr = input().rstrip()
    arr = arr[1:len(arr)-1]
    
    if arr:
        arr = list(map(int, arr.split(",")))
    
    l = 0
    r = max(0,len(arr) - 1)
    isreverserd = False

    iserror = False
    for func in functions:
        
        if func == "R":
            l, r = r,l
            isreverserd = True if isreverserd == False else False

        if func == "D":
            if len(arr) == 0:
                iserror = True
                break

            if -1 == l or l >=len(arr):
                iserror = True
                break

            if isreverserd == True:
                l -= 1
            else:
                l += 1

    if iserror:
        print("error")
    else:
        tmp = []
        if isreverserd:
            tmp = list(reversed(arr[r:l+1]))
        else:
            tmp = list(arr[l:r+1])

        print("[", end="")
        print(*tmp, sep=',', end="")
        print("]")