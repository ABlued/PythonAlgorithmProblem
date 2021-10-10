# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/12939?language=python3
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s))+ " " + str(max(s))

print(solution("1 2 3 4 "))


assert solution("1 2 3 4") == "1 4"
assert solution("-1 -2 -3 -4") == "-4 -1"
assert solution("-1 -1") == "-1 -1"