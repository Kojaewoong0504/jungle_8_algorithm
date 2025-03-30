import sys

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcm(a, b):
    return m * n / gcd(a, b)

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().rstrip().split())
    max_year = lcm(m , n)
    answer = x
    while answer <= max_year: # 멸망해
        if (answer - 1) % n + 1 == y:
            break
        answer += m     # x의 최대값인 m 만큼 증가
    if answer > max_year:
        print(-1)
    else:
        print(answer)