import sys

word = sys.stdin.readline().rstrip()
explosion_string = sys.stdin.readline().rstrip()

stack = []
ex_len = len(explosion_string)

for i in range(len(word)):
    stack.append(word[i])
    if ''.join(stack[-ex_len:]) == explosion_string:
        for _ in range(ex_len):
            stack.pop()

# 결과 출력
if stack:
    print(''.join(stack))
else:
    print('FRULA')