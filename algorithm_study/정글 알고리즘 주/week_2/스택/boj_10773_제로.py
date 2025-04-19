k = int(input())

stack = []

for _ in range(k):
    input_data = int(input())
    if input_data == 0:
        stack.pop()
    else:
        stack.append(input_data)

print(sum(stack))