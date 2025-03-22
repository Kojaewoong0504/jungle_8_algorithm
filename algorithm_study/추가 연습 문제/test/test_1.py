def solution(cylinder, a):
    n = len(cylinder)
    zero_positions = [i for i in range(n) if cylinder[i] == 0]

    if not zero_positions:
        return [0, 1]  # 모든 칸에 총알이 있는 경우

    safe_count = 0
    for start_pos in zero_positions:
        is_safe = True
        current_pos = start_pos
        for _ in range(a):
            current_pos = (current_pos + 1) % n
            if cylinder[current_pos] == 1:
                is_safe = False
                break
        if is_safe:
            safe_count += 1

    # 기약분수 계산
    import math
    gcd = math.gcd(safe_count, len(zero_positions))
    return [safe_count // gcd, len(zero_positions) // gcd]


# 테스트
test_cases = [
    ([1, 1, 0, 0, 0, 0], 2),
    ([1, 0, 0, 0, 0, 1], 2),
    ([0, 0, 0, 0, 0, 0], 1),
    ([1, 0, 1, 0, 1, 0], 1),
    ([0, 0, 0, 0, 0, 0, 0, 0, 1], 4)
]

for cylinder, a in test_cases:
    print(f"Cylinder: {cylinder}, a: {a}")
    print(f"Result: {solution(cylinder, a)}")
    print()