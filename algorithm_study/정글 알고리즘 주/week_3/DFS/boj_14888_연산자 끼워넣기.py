import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split(' ')))
operators = list(map(int, input().split(' ')))
min = 1e9
max = -1e9

def calculator(operand1, operator, operand2):
    if operator == 0:
        return operand1 + operand2
    if operator == 1:
        return operand1 - operand2
    if operator == 2:
        return operand1 * operand2
    if operator == 3:
        if operand1 < 0:
            return - ((-operand1) // operand2)
        else:
            return operand1 // operand2

def dfs(node, value):
    if node == n - 1:
        global min, max
        min = min if min < value else value
        max = max if max > value else value
    else:
        global operators
        for cand in range(4):
            if operators[cand] >= 1:
                operators[cand] -= 1
                dfs(node + 1, calculator(value, cand, nums[node + 1]))
                operators[cand] += 1

dfs(0, nums[0])
print(max)
print(min)