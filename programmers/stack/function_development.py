def solution(progresses, speeds):
    answer = []
    while progresses:
        count = 0
        for index in range(len(progresses)):
            if progresses[index] >= 100 : continue
            progresses[index] += speeds[index]

        while True:
            if progresses and progresses[0] >= 100 :
                del progresses[0]
                del speeds[0]
                count += 1
                continue
            break

        if count != 0 : answer.append(count)
    return answer



progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))