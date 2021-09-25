from itertools import combinations


def solution(orders, course):
    answer = []
    for number_of_orders in course:
        food_ordering_combination = {}
        for i in range (len(orders)):
            combi = list(combinations(orders[i], number_of_orders))

            for order in combi:
                order_string = ''
                for order_element in order:
                    order_string += order_element
                sorting_order_string = ''.join(sorted(order_string))

                if sorting_order_string in food_ordering_combination:
                    food_ordering_combination[sorting_order_string] += 1

                else:
                    food_ordering_combination[sorting_order_string] = 1

        maxValue = max(food_ordering_combination.items(), key=lambda x:x[1])[1]
        for key in food_ordering_combination:
            if maxValue == 1: break
            if food_ordering_combination.get(key) == maxValue:
                answer.append(key)
    return sorted(answer)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution(orders, course))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], 	[2,3,4]))
assert solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]) == ["AC", "ACDE", "BCFG", "CDE"]
assert solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]) == ["ACD", "AD", "ADE", "CD", "XYZ"]
assert solution(["XYZ", "XWY", "WXA"], 	[2,3,4]) == ["WX", "XY"]
