# 실버 5
# 	31256kb	40ms


# import sys
# from collections import deque

# input = sys.stdin.readline

# que_n = deque(list(map(int, input().rstrip())))
# set_count = 1
# visited = [False for _ in range(10)]

# while que_n:
#     front = que_n.popleft()

#     if visited[front] == True:
#         if front == 9 or front == 6:
#             if visited[9] == True and visited[6]  == True:
#                 set_count+=1
#                 visited = [False for _ in range(10)]
#             else:
#                 front = 9 if visited[6] == True else 6

#         else:
#             set_count+=1
#             visited = [False for _ in range(10)]

#     visited[front] = True

# print(set_count)


word = input()
ans = [0] * 10
for i in range(len(word)):
    num = int(word[i])
    if num == 6 or num == 9:
        if ans[6] <= ans[9]:
            ans[6] += 1
        else:
            ans[9] += 1
    else:
        ans[num] += 1

print(max(ans))