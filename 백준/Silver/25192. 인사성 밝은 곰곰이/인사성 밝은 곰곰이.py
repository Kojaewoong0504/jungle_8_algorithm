from collections import defaultdict

n = int(input())

is_enter = False
count = 0
chat_dict = {}

for i in range(n):
    chat = input()
    if chat == "ENTER":
        is_enter = True
        chat_dict = defaultdict(int)
        continue

    if is_enter:
        if chat_dict[chat] == 0:
            count += 1
        chat_dict[chat] += 1

print(count)