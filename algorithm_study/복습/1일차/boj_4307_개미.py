t = int(input())

for _ in range(t):
    l, n = map(int, input().split())  # 막대 길이 l, 개미 수 n
    positions = [int(input()) for _ in range(n)]  # 개미들의 초기 위치
    min_time = 0  # 가능한 가장 빠른 시간
    max_time = 0  # 가능한 가장 느린 시간

    for pos in positions:
        # 빠르게 떨어질 수 있는 시간은 가까운 끝으로 가는 거리
        min_dist = min(pos, l - pos)
        # 느리게 떨어질 수 있는 시간은 먼 쪽 끝으로 가는 거리
        max_dist = max(pos, l - pos)

        min_time = max(min_time, min_dist)
        max_time = max(max_time, max_dist)

    print(f"{min_time} {max_time}")