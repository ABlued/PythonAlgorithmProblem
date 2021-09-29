# 문자열 포메팅

print("I eat %d apples" % 3)
# 문자열 여러 값 포메팅
print( "I ate %d apples. so I was sick for %s days." % (10, "three"))

# 문자열 관련 함수들

# 문자 개수 세기
a = "hobby"
print(a.count('b'))

# 문자 위치 알려주기
# 가장 처음으로 나온 위치만 반환하며 찾는 문자열이 존재하지 않는다면 -1 반환
print(a.find('b'))

# 문자열 삽입
print(",".join('abcd'))

# 문자열 나눠 리스트로 만들기
print("Life is too short".split())

# 리스트를 문자열로 바꾸기
print(''.join(['a', 'b', 'c', 'd']))