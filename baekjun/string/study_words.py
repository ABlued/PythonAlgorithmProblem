string = input()
word_ary = [0] * 26
for str in string:
    if 97 <= ord(str):
        word_ary[ord(str)-97] += 1
    else :
        word_ary[ord(str)-65] += 1

print("?") if word_ary.count(max(word_ary)) > 1 else print(chr(65 + word_ary.index(max(word_ary))))