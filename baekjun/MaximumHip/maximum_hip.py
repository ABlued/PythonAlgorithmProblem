# 문제 링크 : https://www.acmicpc.net/problem/11279
import heapq

N = int(input())
input_list = [int(input()) for _ in range(N)]
heap = []
heapq.heapify(heap)
for value in input_list:
    if value == 0:
        if len(heap) == 0:
            print(0)
        else :
            print(abs(heapq.heappop(heap)))

    else :
        heapq.heappush(heap, -value)

