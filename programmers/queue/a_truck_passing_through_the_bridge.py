from collections import deque

def solution(bridge_length, weight, truck_weights):
    count = 0
    bridge = deque(0 for _ in range(bridge_length))
    bridge_weights = 0
    while truck_weights:
        bridge_weights -= bridge.popleft()
        if bridge_weights + truck_weights[0] <= weight:
            bridge_weights += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else :
            bridge.append(0)
        count += 1

    count += bridge_length
    return count


bridge_length = 10
weight = 10
truck_weights = [1,2,3,4,5]

print(solution(bridge_length, weight, truck_weights))
