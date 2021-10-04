# 문제링크 : https://programmers.co.kr/learn/courses/30/lessons/68645?language=python3
def solution(n):
    # 1
    res = [[0] * n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1

    # 2
    for i in range(n):
        for j in range(i, n):
            # 3
            # down
            if i % 3 == 0:
                x += 1

            # right
            elif i % 3 == 1:
                y += 1

            # up
            elif i % 3 == 2:
                x -= 1
                y -= 1
            # 4
            res[x][y] = num
            num += 1

    for i in res:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer

n = 4
print(solution(n))
assert solution(4) == [1,2,9,3,10,8,4,5,6,7]
assert solution(5) == [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
assert solution(6) == [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
