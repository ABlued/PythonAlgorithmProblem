# 문제 링크 : https://www.acmicpc.net/problem/1260
from collections import deque

def dfs_stack(road_map, start_node):
    stack = [start_node]
    visited = []
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
        for i in range(0,len(road_map[current_node])):
            if road_map[current_node][i] not in visited:
                stack.append(road_map[current_node][i])

    for value in visited:
        print(value, end=' ')
    print()
    return visited

def bfs_queue(road_map, start_node):
    queue = deque([start_node])
    visited = []

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.append(current_node)
        for i in range(len(road_map[current_node])-1,-1,-1):
            if road_map[current_node][i] not in visited:
                queue.append(road_map[current_node][i])
    for value in visited:
        print(value, end=' ')
    print()
    return visited


node, edge, start_node = map(int, input().split())
road_ary = []
road_map = {}
for i in range(edge):
    road_ary.append(list(map(int, input().split())))

for i in range(1, node+1):
    road_map[i] = []

for i in range(len(road_ary)):
    for j in range(len(road_ary[i])):
        if road_ary[i][1] not in road_map[road_ary[i][0]]:
            road_map[road_ary[i][0]].append(road_ary[i][1])
            road_map[road_ary[i][1]].append(road_ary[i][0])

for i in range(1, len(road_map)+1):
    road_map[i] = sorted(road_map[i],reverse=True)

dfs_stack(road_map,start_node)
bfs_queue(road_map,start_node)

assert dfs_stack({1: [4, 3, 2], 2: [4, 1], 3: [4, 1], 4: [3, 2, 1]},1) == [1, 2, 4, 3]
assert bfs_queue({1: [4, 3, 2], 2: [4, 1], 3: [4, 1], 4: [3, 2, 1]},1) == [1, 2, 3, 4]

assert dfs_stack({1: [3, 2], 2: [5, 1], 3: [4, 1], 4: [5, 3], 5: [4, 2]},3) == [3, 1, 2, 5, 4]
assert bfs_queue({1: [3, 2], 2: [5, 1], 3: [4, 1], 4: [5, 3], 5: [4, 2]},3) == [3, 1, 4, 2, 5]

assert dfs_stack({999: [1000], 1000: [999]}, 1000) == [1000, 999]
assert bfs_queue({999: [1000], 1000: [999]}, 1000) == [1000, 999]