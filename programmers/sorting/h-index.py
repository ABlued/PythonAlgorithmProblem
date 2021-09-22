def solution(citations):
    citations.sort()
    citations_len = len(citations)
    for i in range(citations_len):
        if citations[i] >= citations_len-i:
            # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return citations_len-i
    return 0

citations = [0,0,0,1,1,0]
print(solution(citations))
assert solution([3,0,6,1,5]) == 3
assert solution([0,0,0,1,0,1]) == 1
assert solution([0,0,0,0]) == 0
