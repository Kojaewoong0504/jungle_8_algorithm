N, M = map(int, input().split())
J = int(input())

left = 1
right = M
move = 0

for _ in range(J):
    x = int(input())

    if x < left:
        move += left - x
        right -= left - x
        left = x

    elif x > right:
        move += x - right
        left += x - right
        right = x

print(move)