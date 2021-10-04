from itertools import product

def solution(word):
    dic_word = ['A', 'E', 'I', 'O', 'U']
    dic_collection = []
    dic_collections = []
    string_collections = []

    for _ in range(5):
        dic_collection.append(dic_word)
        dic_collections.append(list(product(*dic_collection)))

    for i in range(len(dic_collections)):
        for j in range(len(dic_collections[i])):
            words = ''
            for k in range(len(dic_collections[i][j])):
                words += dic_collections[i][j][k]
            string_collections.append(words)

    return sorted(string_collections).index(word) + 1




assert solution("AAAAE") == 6
assert solution("AAAE") == 10
assert solution("I") == 1563
assert solution("EIO") == 1189