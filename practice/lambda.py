# lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다. 보통 함수를 한줄로 간결하게 만들 때 사용한다.
# 우리말로는 "람다"라고 읽고 def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.

# 사용법 : lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식

add = lambda a, b : a+b
print(add(3,4))

# 짝수와 홀수를 람다와 삼항연산자를 통해 간략하게 만들어보기
solution = lambda a : print("짝수다") if a%2==0 else print("홀수다")
input = int(input())
solution(input)