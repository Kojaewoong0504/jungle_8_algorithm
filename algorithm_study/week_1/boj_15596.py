n = int(input())
a = list(map(int, input().split()))


def solve(a: list) -> int:
    return sum(a)


print(solve(a))
