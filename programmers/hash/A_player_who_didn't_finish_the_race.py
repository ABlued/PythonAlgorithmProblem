# def solution(participant, completion):
#
#     for value in completion:
#         participant.remove(value)
#
#     return participant
#

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for index in range(len(completion)):
        if participant[index] != completion[index]:
            return participant[index]

    return completion[-1]

participant = ["leo", "kiki", "eden","leo"]
completion = ["eden", "kiki","leo"]

print(solution(participant, completion))
