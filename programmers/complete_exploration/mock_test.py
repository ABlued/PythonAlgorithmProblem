from itertools import cycle
first_student = [1,2,3,4,5]
second_student = [2, 1, 2, 3, 2, 4, 2, 5]
third_student = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5,]


def solution(answers):
    first_student_cycle = cycle(first_student)
    second_student_cycle = cycle(second_student)
    third_student_cycle = cycle(third_student)
    student_score = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == next(first_student_cycle):
            student_score[0] += 1
        if answers[i] == next(second_student_cycle):
            student_score[1] += 1
        if answers[i] == next(third_student_cycle):
            student_score[2] += 1

    highest_score = max(student_score)
    return [i+1 for i in range(len(student_score)) if student_score[i] == highest_score]

answers = [1,3,2,4,2]
print(solution(answers))