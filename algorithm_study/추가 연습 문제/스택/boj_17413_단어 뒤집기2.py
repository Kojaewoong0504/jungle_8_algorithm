# # input_string = list(input().split(" "))
# input_string = input()
# memory_string = ""
#
# stack = []
# tag_string = ""
# for i in input_string:
#     if i in "<>":
#         if i == "<":
#             stack.append(i)
#         else:
#             stack.pop()
#             tag_string += i
#             continue
#     if stack and stack[-1] == "<":
#         tag_string += i
#         continue
#     stack.append(i)
# memory_string = "".join(stack)
# split_word = memory_string.split(" ")
# result = []
# for word in split_word:
#     result.append(word[::-1])
# split_tag = []
# tag_stack = []
# if tag_string:
#     for i in tag_string:
#         if i in "<>":
#             if i == "<":
#                 tag_stack.append(i)
#                 continue
#             else:
#                 tag_stack.append(i)
#                 split_tag.append("".join(tag_stack))
#                 tag_stack = []
#                 continue
#         if tag_stack and tag_stack[0] == "<":
#             tag_stack.append(i)
#     print(split_tag[0] + " ".join(result) + split_tag[-1])
# else:
#     print(" ".join(result))


input_string = input()
result = ""
i = 0
n = len(input_string)

while i < n:
    # 태그인 경우
    if input_string[i] == '<':
        j = i
        while j < n and input_string[j] != '>':
            j += 1
        if j < n:  # '>'를 찾은 경우
            result += input_string[i:j + 1]  # 태그는 그대로 추가
            i = j + 1
        else:  # '>'를 찾지 못한 경우 (비정상적인 입력)
            result += input_string[i]
            i += 1
    # 태그가 아닌 경우 (단어 또는 공백)
    else:
        j = i
        while j < n and input_string[j] != '<' and input_string[j] != ' ':
            j += 1

        # 단어를 뒤집어서 추가
        if j > i:
            result += input_string[i:j][::-1]
            i = j

        # 공백 처리
        if i < n and input_string[i] == ' ':
            result += ' '
            i += 1

print(result)
