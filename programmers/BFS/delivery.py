# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/12978?language=python3

import math
def solution(N, road, K):
    answer = 0
    roads = [[math.inf for i in range(N)] for j in range(N)]
    for r in road:
        if roads[r[1] - 1][r[0] - 1] > r[2]:
            roads[r[1] - 1][r[0] - 1] = r[2]
            roads[r[0] - 1][r[1] - 1] = r[2]

    for i in range(N):
        roads[i][i] = 0

    for path in range(N):
        for i in range(N):
            for j in range(N):
                if roads[i][j] > roads[i][path] + roads[path][j]:
                    roads[i][j] = roads[i][path] + roads[path][j]

    for i in range(N):
        if roads[0][i] <= K:
            answer += 1

    return answer
# N = 5
# road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
# K = 3
# print(solution(N, road, K))

assert solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3) == 4
assert solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1],[1,6,1]], 4) == 5
assert solution(2,[[1,2,1]],1) == 2

# 내가 푼 풀이(점수는 60점대)

# from collections import deque
# def solution(N, road, K):
#     answer = 0
#     map = {}
#
#     delivery_place = [1]
#     for i in range(1,N+1):
#         map[i] = [0 for _ in range(1,N+1)]
#
#     for road_data in road:
#         if map[road_data[0]][road_data[1] - 1] == 0 or road_data[2] < map[road_data[0]][road_data[1] - 1]:
#             map[road_data[0]][road_data[1] - 1] = road_data[2]
#             map[road_data[1]][road_data[0] - 1] = road_data[2]
#
#     queue = deque([[i+1,map[1][i]] for i in range(len(map[1])) if map[1][i] != 0])
#     for i in range(len(map[1])):
#         if 0 < map[1][i] and map[1][i] <= K:
#             delivery_place.append(i+1)
#
#     print(queue)
#     while queue:
#         popValue = queue.popleft()
#
#         for i in range(len(map[popValue[0]])):
#             if map[popValue[0]][i] == 0:
#                 continue
#             if i+1 not in delivery_place and popValue[1] + map[popValue[0]][i] <= K:
#                 queue.append([i+1, popValue[1] + map[popValue[0]][i]])
#                 delivery_place.append(i+1)
#
#     for v in map.values():
#         print(v)
#     print(delivery_place)
#     return len(delivery_place)