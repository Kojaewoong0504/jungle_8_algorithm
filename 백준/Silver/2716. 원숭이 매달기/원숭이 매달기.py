t = int(input())

for _ in range(t):
    case = input()
    if case == "":
        print(1)
        continue
    depth = 0
    max_depth = 0

    for i in case:
        if i == "[":
            depth += 1
            max_depth = max(depth, max_depth)
        elif i == "]":
            depth -= 1
    print(2**max_depth)