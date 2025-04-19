import sys
from collections import defaultdict

input = sys.stdin.readline


def can_place_banner():
    n, m = map(int, input().split())
    heights = list(map(int, input().split()))

    # 필요한 같은 높이의 최소 개수
    required_count = (9 * m + 9) // 10

    # 각 높이 값의 등장 위치 기록
    height_positions = defaultdict(list)
    for i, h in enumerate(heights):
        height_positions[h].append(i)

    # 각 높이 값에 대해 검사
    for positions in height_positions.values():
        if len(positions) < required_count:
            continue

        # 슬라이딩 윈도우로 연속된 M 구간 내 위치 확인
        for i in range(len(positions) - required_count + 1):
            start_idx = positions[i]
            end_idx = positions[i + required_count - 1]

            if end_idx - start_idx < m:
                return "YES"

    return "NO"


print(can_place_banner())
