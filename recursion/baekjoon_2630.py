import sys


def recur(x, y, size):
    global arr, result

    if 1 == size:
        return arr[x][y]
    
    v = [0,0,0]

    v[recur(x, y, size//2)] += 1
    v[recur(x+size//2, y, size//2)] += 1
    v[recur(x, y + size//2, size//2)] += 1
    v[recur(x+size//2, y + size//2, size//2)] += 1

    # v  = [white, blue, 통일X(사실상 쓰레기값)]
    for i in range(2):
        if v[i] != 4 and v[i] != 0:
            result[i] += v[i]

        else:
            if v[i] == 4:
                return i
            
    return 2
            

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = [ list(map(int, input().split(" "))) for i in range(n)]

    result = [0,0]
    recur(0,0,n)
    for r in result:
        print(r)