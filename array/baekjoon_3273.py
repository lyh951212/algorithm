import sys
input = sys.stdin.readline

## 이진탐색 방식
# def binary_search(l,r,findn):

#     if l > r:
#         return 0
    
#     mid = (l + r) //2

#     if arr[mid] == findn:
#         return 1
    
#     if arr[mid] > findn:
#         return binary_search(l, mid-1,findn)
#     else:
#         return binary_search(mid+1, r,findn)
    

# size = int(input())
# arr = sorted(list(map(int, input().split(" "))))
# x = int(input())
# cnt = 0

# for i in range(size):
#     if arr[i] >= x or arr[i]*2 == x:
#         continue
#     find_n = x-arr[i]
#     cnt += binary_search(0, len(arr)-1, find_n)

# print(cnt//2)


## ---------------------------------------------------------

## 투포인터 방식

size = int(input())
arr = sorted(list(map(int, input().split(" "))))
x = int(input())
cnt = 0

i = 0
j = len(arr)-1
while i!= j:
    if arr[i] + arr[j] == x:
        cnt += 1
        i+=1

    elif arr[i] + arr[j] > x:
        j -= 1
    else:
        i += 1

print(cnt)