import sys
from collections import deque

# 다리 위의 트럭의 전체 무게를 구하는 함수
def sum_trucks_weight_on_bridge():
    global bridge
    sum = 0
    for b in bridge:
        sum += b[0]
    return sum

if __name__ == "__main__":
    n,w,L = map(int, input().split(" "))
    wait = deque(list(map(int, input().split(" "))))

    bridge = list()
    time = 0
    while wait:
        # 다리에서 탈출
        if bridge and bridge[0][1] >= w:
            bridge.pop(0)

        # 다리 위에 트럭이 있으면 - 앞으로 가거나 위에 트럭을 더 올리거나 해야함
        # 트럭을 다리위에 더 올릴 수 있는 상황
        if wait and sum_trucks_weight_on_bridge() + wait[0] <= L and len(bridge) < w:
            # 트럭을 다리위에 더 올리기 전에 앞에 있는 트럭들을 한칸씩 이동시킨다.
            for b in bridge:
                b[1] += 1
            # [트럭 무게, 현재 트럭이 위치한 곳. 시작점부터 1로 시작]
            bridge.append([wait.popleft(),1])
        else:
            # 다리에 트럭을 더 못 올리기 때문에 한칸식 이동만 시킨다.
            for b in bridge:
                b[1] += 1

        time += 1

    # 다리위에 트럭들이 남았을 때
    while bridge:
        if bridge and bridge[0][1] >= w:
            bridge.pop(0)

        for b in bridge:
            b[1] += 1

        time += 1

    print(time)
