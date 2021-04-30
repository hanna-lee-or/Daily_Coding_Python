# 프로그래머스 Level2 다리를 지나는 트럭
# 모든 트럭이 다리를 건너는 최소 시간(초)
# 트럭은 리스트 순서대로 다리에 진입하며, 1초에 1만큼 움직인다.
# 다리는 weight 무게까지 견딜 수 있다.
# [!] 트럭이 다리에 완전히 오르지 않은 경우, 트럭 무게 고려 X

from collections import deque


class TruckInfo:

    def __init__(self, weight, entry_time):
        self.weight = weight
        self.entry_time = entry_time

    def __iter__(self):
        return self


def solution(bridge_length, weight, truck_weights):

    # 다리에 진입하는 트럭 무게와 진입 시간을 표시한다.
    bridge_q = deque()
    bridge_q.append(TruckInfo(truck_weights[0], 1))
    # 현재 시간, 다리 무게
    current_time = 1
    current_w = truck_weights[0]

    # 다음에 진입할 트럭의 idx
    i = 1
    truck_num = len(truck_weights)
    while i < truck_num:
        current_time += 1
        # 다리를 건너면 큐에서 제거
        target = bridge_q[0]
        if current_time - target.entry_time >= bridge_length:
            print(f'{current_time}초 : 트럭({target.weight}) 다리 끝')
            current_w -= target.weight
            bridge_q.popleft()
        # 트럭 다리에 진입시키기 (가능한 경우)
        if current_w + truck_weights[i] <= weight:
            print(f'{current_time}초 : 트럭({truck_weights[i]}) 다리 진입')
            current_w += truck_weights[i]
            bridge_q.append(TruckInfo(truck_weights[i], current_time))
            i += 1
    
    return current_time + bridge_length


print(solution(2, 10, [7, 4, 5, 6]))  # 8


# 다른 사람 풀이. Bridge 클래스를 만든 것이 핵심.
"""

import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()
"""


