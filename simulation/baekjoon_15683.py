import sys

def solution():
    

if __name__ == "__main__":
    input = sys.stdin.readline
    r,c = map(int, input().split(" "))
    
    arr = [ list(map(int,input().split(" "))) for i in range(r)]

    dir = dict()
    dir[1] = [[1,0], [0,1], [-1,0], [0,-1]] # 4개
    dir[2] = [[[-1,0], [1,0]], [ [0,1], [0,-1]]] # 2개
    dir[3] = [[[0,-1], [1,0]], [ [1,0], [0,1]], [ [-1,0], [0,1]], [ [0,-1], [-1,0]]] # 4개
    dir[4] = [
        [ [-1,0], [0,-1], [1,0]], 
        [ [0,-1], [1,0],  [0,1]], 
        [ [-1,0], [0,1],  [1,0]], 
        [ [-1,0], [0,-1], [0,1]]
        ] # 4개
    dir[5] = [[ [-1,0], [1,0],  [0,1], [0,-1]]] # 1개

    solution()