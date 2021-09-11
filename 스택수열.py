# input1 = int(input())
# input2= []
# stack = []
# result = ['+']
# for i in range (0,input1):
#     input2.append(int(input()))
# count = 2
# stack = [1]
# while input2 and stack[len(stack) - 1] <= input2[0]:
#
#     if input2[0] != stack[len(stack) - 1]:
#         stack.append(count)
#         result.append('+')
#         count += 1
#     elif input2[0] == stack[len(stack) - 1]:
#         result.append('-')
#         input2.pop(0)
#         stack.pop()
#
#     if not stack and input2 :
#         stack.append(count)
#         result.append('+')
#         count += 1
#
# if len(input2) == 0:
#     for value in result:
#         print(value)
# else: print("NO")



def stack_sequence(n, sequence):
    stack = []
    num = 1
    sequence_idx = 0
    result = []
    while True:
        if len(stack) == 0:
            stack.append(num)
            result.append("+")
            num += 1
        elif sequence[sequence_idx] == stack[-1]:
            stack.pop()
            result.append("-")
            sequence_idx += 1
            if sequence_idx == n:
                break
        else:
            if n < num:
                print("NO")
                break
            stack.append(num)
            result.append("+")
            num += 1

    if len(stack) == 0:
        for char in result:
            print(char)

sequence = list()
n = int(input())
for _ in range(n):
    sequence.append(int(input()))
stack_sequence(n, sequence)