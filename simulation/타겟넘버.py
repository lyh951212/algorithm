def dfs(curidx, curres, numbers, target):
    if curidx == len(numbers):
        if curres == target:
            return 1
        return 0
    
    return dfs(curidx+1, curres + numbers[curidx], numbers , target) + dfs(curidx+1, curres - numbers[curidx], numbers , target)
        
def solution(numbers, target):
    answer = dfs(0,0,numbers, target)
    return answer