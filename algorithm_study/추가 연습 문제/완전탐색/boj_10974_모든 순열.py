from itertools import permutations

n = int(input())
total = [i for i in range(1,n+1)]
permutation_list = permutations(total, n)

for result in sorted(permutation_list):
    for i in result:
        print(i, end=" ")
    print("")

