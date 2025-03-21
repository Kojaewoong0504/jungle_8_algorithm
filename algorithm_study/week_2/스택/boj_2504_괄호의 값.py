input_datas = input()


def func():
    stack = []

    for char in input_datas:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            # 스택이 비어있거나 짝이 맞지 않으면 올바르지 않은 괄호열
            if not stack:
                return 0

            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
            else:
                temp_sum = 0
                while stack and isinstance(stack[-1], int):
                    temp_sum += stack.pop()

                if not stack or stack[-1] != '(':
                    return 0

                stack.pop()  # '(' 제거
                stack.append(temp_sum * 2)

        elif char == ']':
            # 스택이 비어있거나 짝이 맞지 않으면 올바르지 않은 괄호열
            if not stack:
                return 0

            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
            else:
                temp_sum = 0
                while stack and isinstance(stack[-1], int):
                    temp_sum += stack.pop()

                if not stack or stack[-1] != '[':
                    return 0

                stack.pop()  # '[' 제거
                stack.append(temp_sum * 3)

    # 스택에 괄호가 남아있으면 올바르지 않은 괄호열
    if any(not isinstance(item, int) for item in stack):
        return 0

    # 스택에 남은 숫자들의 합이 최종 괄호값
    return sum(stack)


print(func())
