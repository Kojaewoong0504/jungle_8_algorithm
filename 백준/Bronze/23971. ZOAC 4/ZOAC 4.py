import math

H, W, N, M = map(int, input().split())

# 세로 방향으로 앉을 수 있는 최대 인원 수
vertical = math.ceil(H / (N + 1))

# 가로 방향으로 앉을 수 있는 최대 인원 수
horizontal = math.ceil(W / (M + 1))

# 총 수용 가능 인원 수
total = vertical * horizontal

print(total)
