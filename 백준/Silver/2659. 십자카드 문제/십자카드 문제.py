import sys

nums = list(map(int, sys.stdin.readline().split()))

def get_clock_num(n):
    min = int(''.join(map(str, n)))
    for i in range(1,4):
        tmp = int(''.join(map(str, n[i:]+n[:i])))
        if min > tmp:
            min = tmp
    return min

clk_num = get_clock_num(nums)
cnt = 1

for i in range(1111, clk_num):
    if '0' not in list(str(i)) and i == get_clock_num(list(map(int, str(i)))):
        cnt += 1
print(cnt)