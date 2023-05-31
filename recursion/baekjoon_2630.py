import sys

def recur(x, y, size):
    global n, arr, result

    if size == 1:
        return arr[x][y]
    
    v = [0,0,0]
    for i in range(2):
        for j in range(2):
            v[recur(x + i*(size//2), y + j*(size//2), size//2)] += 1

    # 바로 결과에 반영
    if v[0] != 4 and v[1] != 4:
        result[0] += v[0]
        result[1] += v[1]
        return 2
    else:
        for i in range(2):
            if v[i] == 4:
                return i

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    arr = [ list(map(int, input().split(" "))) for i in range(n)]

    result = [0,0]
    ret = recur(0,0,n)
    if ret != 2:
        result[ret] += 1

    for r in result:
        print(r)