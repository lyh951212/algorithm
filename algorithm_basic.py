# dfs
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end= ' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# bfs
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    # node visited
    visited[start] = True

    # loop till queue is empty
    while queue:
        # visted node 'v' 
        v = queue.popleft()
        print(v, end=' ')

        # v 노드에 연결된 노드들 투입 -> 방문 안한 노드만 queue에 추가
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                # print(queue) # queue안에 뭐있나
                visited[i] = True

# 정렬 알고리즘
## python의 sorted함수는 내부적으로 병합정렬을 사용한다.


# 다이나믹 프로그래밍
## 문제 특징
### 1. 큰 문제를 작은 문제로 나눌 수 있다.
### 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

# 재귀를 이용하여 큰 문제부터 작은 문제를 해결해나가는 Top-Down 방식, 메모이제이션(Memoization) 방식으로 풀 수 있다.

d = [0] * 100 # Memoization 초기화

def fibo(x):
    # base case
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    # 점화식을 그대로 구현
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

# 반복문을 이용하여 작은 문제부터 답을 도출하는 Bottom-Up(보텀업) 방식으로 풀어볼 수 있다.
# initiate DP Table
d = [0] * 100
# both first Fibonacci number and second fibonacci number are 1
d[1] = 1
d[2] = 1
n = 99
# bottom up dynamic programming
for i in range(3, n+1):
    d[i] = d[i - 1] + d[i - 2]