import sys

N = int(sys.stdin.readline())

pokemon_list = [0] * N

max_count = 0
total_count = 0

for i in range(N):
    P = sys.stdin.readline().rstrip()
    K, M = map(int, sys.stdin.readline().split())

    each_count = 0

    while K <= M:
        M -= K - 2
        each_count += 1
    
    if max_count < each_count:
        max_count = each_count

    pokemon_list[i] = (P, each_count)

    total_count += each_count

target_pokemon = ''

for pokemon, count in pokemon_list:
    
    if count == max_count:
        target_pokemon = pokemon
        break

print(total_count)
print(pokemon)