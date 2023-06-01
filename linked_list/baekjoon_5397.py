import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    input_pw = map(str, input().rstrip())
    left = list()
    right = list()
    
    for s in input_pw:
        if s == "<":
            # 왼쪽에 있는거 오른쪽으로 
            if left:
                right.append(left.pop())
        elif s == ">":
            # 오른쪽에 있는거 왼쪽으로 
            if right:
                left.append(right.pop())
        elif s == "-":
            if left:
                left.pop()
        else:
            left.append(s)
            
    left.extend(reversed(right))
    print(''.join(left))

