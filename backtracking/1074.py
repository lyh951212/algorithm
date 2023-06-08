
import sys

def recur(x,y,n,start):
    print(x,y,n,start)
    if n == 0:
        return start
    
    a = 2**n // 2
    _x = x // a 
    _y = y // a
    

    next_x = x % a
    next_y = y % a

    area = 0
    if _x >= 1 and _y >= 1: # 1사분면
        area = 4
    elif _x >= 1 and _y < 1:
        area = 3
    elif _x < 1 and _y >= 1:
        area = 2
    elif _x < 1 and _y < 1:
        area = 1

    start = start + a**2 * (area-1)

    return recur(next_x, next_y, n-1, start)


#main
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N, r, c = map(int , input().split(" "))

print(recur(r,c,N,0))