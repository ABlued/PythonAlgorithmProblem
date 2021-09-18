import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1: return -1
        smallest_scoville, next_small_scoville = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, smallest_scoville + (next_small_scoville * 2 ))
        answer += 1

    return answer

scoville = [1,1]
K = 7
print(solution(scoville, K))