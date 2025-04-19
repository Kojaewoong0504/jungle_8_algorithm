ir = input()
stack = []
cnt = 0
for i in range(len(ir)):
    if ir[i] == "(":
        stack.append("(")
    else:
        stack.pop()
        if ir[i - 1] == "(":
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)