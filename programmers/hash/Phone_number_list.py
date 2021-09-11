def solution(phone_book):
    dic = {}

    for i in range(len(phone_book)):
        for j in range(len(phone_book[i])):
            if phone_book[i][:j + 1] in dic: return False
        dic[phone_book[i]] = 1

    for i in range(len(phone_book)):
        for j in range(len(phone_book[i])):
            if phone_book[i][:j + 1] in dic and dic[phone_book[i][:j + 1]] == 2  : return False
            elif phone_book[i][:j + 1] in dic : dic[phone_book[i]] = 2

    return True


phone_book = ["12345","12","456","789","4123"]
print(solution(phone_book))