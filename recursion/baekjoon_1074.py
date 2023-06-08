import sys

def recur( size):
    global R, C
    if size == 1:
        return R * 2 + C

    area = (size//2) * (size//2) 
    _r = R//(size/2)
    _c = C//(size/2)

    R -= (size//2) * _r
    C -= (size//2) * _c 

    return area * (_r * 2 + _c) + recur(size//2)


if __name__ == "__main__":
    input = sys.stdin.readline
    n, R, C = map(int, input().split(" "))
    
    print( int(recur(2**n)))