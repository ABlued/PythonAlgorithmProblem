# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3
from collections import deque

def solution(priorities, location):
    location = location + 1
    answer = 0
    queue = deque(value for value in priorities)

    while len(queue) > 1:
        popValue = queue.popleft()
        if popValue >= max(queue):
            if location == 1:
                return 1 + answer
            else:
                location -= 1
                answer += 1
        else :
            queue.append(popValue)
            if location == 1:
                location += len(queue) - 1
            else : location -= 1


    return 1 + answer

priorities = [2, 1, 3, 2, 1]
location = 4

print(solution(priorities, location))

assert solution([2, 1, 3, 2], 2) == 1
assert solution([2, 1, 3, 2, 1], 4) == 5
assert solution([1, 1, 9, 1, 1, 1], 0) == 5