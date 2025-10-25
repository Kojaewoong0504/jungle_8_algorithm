import sys

def next_power_of_two(x: int) -> int:
    # x >= 1
    return x if (x & (x - 1)) == 0 else 1 << (x - 1).bit_length()

out = []
for line in sys.stdin:
    G, T, A, D = map(int, line.split())
    if G == -1 and T == -1 and A == -1 and D == -1:
        break

    group_matches = G * (T * (T - 1) // 2)
    P0 = G * A + D
    P = next_power_of_two(P0)
    Y = P - P0
    tournament_matches = P - 1
    X = group_matches + tournament_matches

    out.append(f"{G}*{A}/{T}+{D}={X}+{Y}")

print("\n".join(out))
