import sys
input = sys.stdin.readline

word = input().rstrip()
explosion_string = input().rstrip()

stack = []
bomb_len = len(explosion_string)

for i in range(len(word)):
    stack.append(word[i])
    if ''.join(stack[-bomb_len:]) == explosion_string:
        for _ in range(bomb_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')