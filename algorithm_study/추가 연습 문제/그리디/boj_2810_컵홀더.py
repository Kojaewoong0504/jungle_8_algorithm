from collections import defaultdict
n = int(input())

sit_list = input()

sit_dict = defaultdict(int)
for sit in sit_list:
    sit_dict[sit] += 1

can_cup = (sit_dict["L"] // 2) + sit_dict["S"] + 1

if can_cup > n:
    print(n)
else:
    print(can_cup)
