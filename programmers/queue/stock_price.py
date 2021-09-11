from collections import deque
prices = [1,2,3,2,3]
def solution(prices):
    answer = []

    prices_deque = deque(prices)
    while prices_deque:
        current_price = prices_deque.popleft()
        count = 0
        for next_price in prices_deque:
            if current_price > next_price:
                count += 1
                break
            count += 1
        answer.append(count)


    return answer

print(solution(prices))

# from collections import deque
#
#
# def solution(prices):
#     answer = []
#     prices_deque = deque(prices)
#
#     while len(prices_deque) != 0:
#         current_number = prices_deque.popleft()
#         count = 0
#         for index in range(len(prices_deque)):
#             if current_number > prices_deque[index]:
#                 count += 1
#                 break
#             count += 1
#         answer.append(count)
#     return answer

# 스택으로 풀어낸 예시(시간복잡도가 O(n)이다)


# def solution(prices):
#     stack = []
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         if stack != []:
#             while stack != [] and stack[-1][1] > prices[i]:
#                 past, _ = stack.pop()
#                 answer[past] = i - past
#         stack.append([i, prices[i]])
#     for i, s in stack:
#         answer[i] = len(prices) - 1 - i
#     return answer