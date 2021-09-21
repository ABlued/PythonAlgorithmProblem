from collections import deque

def solution(n, computers):
    answer = 0
    network_list = [1 for _ in range(len(computers))]
    queue = deque([computers[0]])
    while 1 in network_list:
        while queue:
            for i in range(len(network_list)):
                if queue[0][i] == 1 and network_list[i] != -1:
                    network_list[i] = - 1
                    queue.append(computers[i])
            queue.popleft()

        answer+=1
        if 1 in network_list:
            queue.append(computers[network_list.index(1)])

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))