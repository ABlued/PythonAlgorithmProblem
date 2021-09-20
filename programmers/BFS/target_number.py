from collections import deque
def solution(numbers, target):
    queue = deque([numbers[0], -numbers[0]])

    for i in range(1,len(numbers)):
        for _ in range (len(queue)):
            popValue = queue.popleft()
            queue.append(popValue + numbers[i])
            queue.append(popValue - numbers[i])

    return queue.count(target)


numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))