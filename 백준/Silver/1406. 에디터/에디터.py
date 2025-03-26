word = list(map(str, input()))
n = int(input())

orders = []

for _ in range(n):
    orders.append(list(map(str, input().split())))

r_list = []
for order in orders:
    if order[0] == "L":
        if word:
            r_list.append(word.pop())
    elif order[0] == "D":
        if r_list:
            word.append(r_list.pop())
    elif order[0] == "B":
        if word:
            word.pop()
    elif order[0] == "P":
        word.append(order[1])
word.extend(reversed(r_list))
print(''.join(word))