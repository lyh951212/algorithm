import sys
input = sys.stdin.readline

def calculate_minus_and_zero():
    global minus_and_zero
    
    minus_and_zero.sort()
    minus_and_zero = sorted(minus_and_zero, key = abs)

    cur_cal = []
    res = 0
    while minus_and_zero: 
        cur_cal.append(minus_and_zero.pop())

        if len(cur_cal) == 2: 
            s = sum(cur_cal)
            m = cur_cal[0] * cur_cal[1]
            res += max(s,m)
            cur_cal.clear()

    if cur_cal:
        res += cur_cal.pop()

    return res


if __name__ == "__main__":
    n = int(input())
    stack = list()
    minus_and_zero = list()
    for _ in range(n):
        num = int(input())
        if num > 0:
            stack.append(num)
        else:
            minus_and_zero.append(num)

    calres = calculate_minus_and_zero()
    # stack.append(calres) ## 규칙에 위배된다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # 절대값 순으로 정렬하기기
    stack.sort()
    stack = sorted(stack, key = abs)

    ans = 0
    cur_cal = []
    while stack:  
        cur_cal.append(stack.pop())

        if len(cur_cal) == 2:
            s = sum(cur_cal) 
            m = cur_cal[0] * cur_cal[1] 
            ans += max(s,m) 
            cur_cal.clear()

    if cur_cal:
        ans += cur_cal.pop()

    print(ans + calres)
