import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x,result):
    visited[x] = True
    cycle.append(x) #사이클을 이루는 팀을 확인하기 위함
    number = arr[x]
    
    if visited[number]: #방문가능한 곳이 끝났는지
        if number in cycle: #사이클 가능 여부
            result += cycle[cycle.index(number):] #사이클 되는 구간 부터만 팀을 이룸
        return
    else:
        dfs(number,result)

for _ in range(int(input())):
    n =  int(input())
    arr = [0] + list(map(int,input().split()))
    visited=[False for _ in range(n+1)]
    result = []
    
    for i in range(1,n+1):
        if not visited[i]: #방문 안한 곳이라면
            cycle = []
            dfs(i,result) #DFS 함수 돌림
    
    print(n - len(result)) #팀에 없는 사람 수