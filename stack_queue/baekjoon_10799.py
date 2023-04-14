import sys

def count_sticks(parens):
    stack = []
    res = 0
    for i, p in enumerate(parens):
        if p == "(":
            stack.append(i)
        else:
            if stack[-1] == i - 1:
                # 레이저일 경우, 스택에서 pop하여 현재 쇠막대기의 개수를 더합니다.
                stack.pop()
                res += len(stack)
            else:
                # 쇠막대기의 끝인 경우, 스택에서 pop하여 쇠막대기의 개수를 1 증가시킵니다.
                stack.pop()
                res += 1
    return res

if __name__ == "__main__":
    arr = list(input())
    
    # close = []

    # lazer = []
    # stick = []

    # for i in range(len(arr)-1, -1 , -1): ####!!!
    #     if arr[i] == ")":
    #         close.append(i)
    #     else:
    #         if close[-1] - i == 1:
    #             lazer.append(i)
    #             close.pop()
    #         else:
    #             # 쇠막대기
    #             stick.append((i, close.pop()))

    # res = 0
    # for s in stick:
    #     count = 1
    #     for l in lazer:
    #         if s[0] < l < s[1] and s[0] < l+1 < s[1]:
    #             count += 1

    #     res += count

    print(count_sticks(arr))