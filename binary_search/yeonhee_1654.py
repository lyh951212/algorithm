import sys
sys.setrecursionlimit(1000000)

def bsearch(l, r):
    global result
    
    mid = (l + r) // 2

    if l > r: # !!!!!!!!
        return 

    length=0
    for i in lan:
        length += (i // mid)


    if length < n :
        bsearch(l,mid-1) # !!!!!!!! mid -1이다
    else:
        result.append(mid)
        bsearch(mid+1, r) # !!!!!!!! mid+1이다
    

if __name__ == "__main__":
    input = sys.stdin.readline
    k, n = map(int, input().split(" "))
    lan = list()
    for i in range(k):
        lan.append(int(input()))

    result = []
    bsearch(1 , max(lan))
    print(max(result))