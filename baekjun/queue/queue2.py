# 문제 링크 : https://www.acmicpc.net/problem/18258
from collections import deque
N = int(input())
queue = deque()
answer = []
for i in range(N):
    operation = input().split()
    if operation[0] == "push":
        queue.append(operation[1])
    elif operation[0] == "pop":
        if len(queue) == 0:
            answer.append(-1)
            continue
        answer.append(queue.popleft())
    elif operation[0] == "size":
        answer.append(len(queue))
    elif operation[0] == "empty":
        if len(queue) != 0:
            answer.append(0)
        else : answer.append(1)
    else :
        if len(queue) == 0:
            answer.append(-1)
            continue
        if operation[0] == "front":
            answer.append(queue[0])
        else :
            answer.append(queue[len(queue) - 1])


for i in range(len(answer)):
    print(int(answer[i]))
