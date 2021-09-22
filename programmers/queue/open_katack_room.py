from collections import deque

def solution(record):
    answer = []
    user_data = {}
    user_access_record = deque()

    for record_data in record:
        record_data = record_data.split()
        user_access_record.append([record_data[0],record_data[1]])
        if record_data[0] == 'Enter' or record_data[0] == 'Change':
            user_data[record_data[1]] = record_data[2]

    for i in range(len(user_access_record)):
        user_access_recore_data = user_access_record.popleft()
        if user_access_recore_data[0] == 'Enter':
            answer.append(user_data[user_access_recore_data[1]] +"님이 들어왔습니다.")
        elif user_access_recore_data[0] == 'Leave':
            answer.append(user_data[user_access_recore_data[1]] + "님이 나갔습니다.")


    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))