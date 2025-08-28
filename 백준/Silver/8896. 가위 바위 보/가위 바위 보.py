t = int(input())

for _ in range(t):
    n = int(input())
    robots = [input().strip() for _ in range(n)]
    k = len(robots[0])

    alive = list(range(n))
    winner = 0

    for r in range(k):
        moves = {robots[i][r] for i in alive}

        if len(moves) == 2:
            if moves == {'R', 'S'}:
                losing = 'S'
            elif moves == {'S', 'P'}:
                losing = 'P'
            elif moves == {'R', 'P'}:
                losing = 'R'

            alive = [i for i in alive if robots[i][r] != losing]

        if len(alive) == 1:
            winner = alive[0] + 1
            break

    if winner == 0 and len(alive) != 1:
        winner = 0
    elif winner == 0 and len(alive) == 1:
        winner = alive[0] + 1

    print(winner)
