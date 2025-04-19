from itertools import combinations

little_man = []
for _ in range(9):
    little_man.append(int(input()))


comb = combinations(little_man, 7)

for i in comb:
    if sum(i) == 100:
        for j in i:
            print(j)
