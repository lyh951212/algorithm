import sys
def r_func():
    global arr
    tmp_dict = [dict() for i in range(len(arr))]
    for i in range(len(arr)):
        for _a in arr[i]:
            if 0 == _a:
                continue
            if _a not in tmp_dict[i].keys():
                tmp_dict[i][_a] = 1
            else:
                tmp_dict[i][_a] += 1

    result = [[] for i in range(len(arr))]
    maxlen = 0
    for i, tmp in enumerate(tmp_dict):
        my_tuples = list(tmp.items())
        my_tuples = sorted(my_tuples, key = lambda x : (x[1], x[0]))
        for tu in my_tuples:
            result[i].append(tu[0])
            result[i].append(tu[1])
        maxlen = max(maxlen, len(result[i]))

    for i, res in enumerate(result):
        cur_len = len(res)
        if cur_len < maxlen:
            for _ in range(maxlen - cur_len):
                res.append(0)

    return result

def c_func():
    global arr
    r = len(arr)
    c = len(arr[0])

    tmp_dict = [dict() for i in range(c)]
    
    for i in range(c):
        for j in range(r):
            n = arr[j][i] 
            if 0 == n:
                continue
            if n not in tmp_dict[i].keys():
                tmp_dict[i][n] = 1
            else:
                tmp_dict[i][n] += 1

    result = [[] for i in range(c)]
    maxlen = 0
    for i, tmp in enumerate(tmp_dict):
        my_tuples = list(tmp.items())    
        my_tuples = sorted(my_tuples, key = lambda x : (x[1], x[0]))
        for tu in my_tuples:
            result[i].append(tu[0])
            result[i].append(tu[1])
        maxlen = max(maxlen, len(result[i]))

    for i, res in enumerate(result):
        cur_len = len(res)
        if cur_len < maxlen:
            for _ in range(maxlen - cur_len):
                res.append(0)

    chg_result = list(zip(*result))
    return chg_result


if __name__ == "__main__":
    input = sys.stdin.readline
    r,c,k = map(int, input().split(" "))
    arr = [ [] for i in range(3)]
    for i in range(3):
        arr[i] = list(map(int, input().split(" ")))

    time = 0
    while time <= 100:
        if r <= len(arr) and c <= len(arr[0]) and arr[r-1][c-1] == k:
            break
        if len(arr) >= len(arr[0]):
            arr = r_func()
        else:
            arr = c_func()
        time += 1
    

    if time > 100:
        if r > len(arr) or c > len(arr[0]):
            time = -1
        elif r <= len(arr) and c <= len(arr[0]) and arr[r-1][c-1] != k:
            time = -1
    print(time)
