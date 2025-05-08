def coin_to_bit(board):
    """3x3 보드(H/T)를 9비트 정수로 변환 (H:0, T:1)"""
    bit = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'T':
                bit |= (1 << (i * 3 + j))
    return bit

def apply_flip(state, mask):
    """mask 위치의 비트를 뒤집기"""
    return state ^ mask

# 각 연산(행, 열, 대각선)에 대응하는 비트마스크 (총 8개)
flip_masks = []

# 3행
for i in range(3):
    mask = 0
    for j in range(3):
        mask |= (1 << (i * 3 + j))
    flip_masks.append(mask)

# 3열
for j in range(3):
    mask = 0
    for i in range(3):
        mask |= (1 << (i * 3 + j))
    flip_masks.append(mask)

# 대각선 ↘
flip_masks.append((1 << 0) | (1 << 4) | (1 << 8))
# 대각선 ↙
flip_masks.append((1 << 2) | (1 << 4) | (1 << 6))

def min_operations(initial):
    min_op = float('inf')
    # 0 ~ 255 모든 연산 조합 시도
    for bits in range(1 << 8):  # 2^8
        state = initial
        cnt = 0
        for i in range(8):
            if bits & (1 << i):  # i번째 연산 적용
                state = apply_flip(state, flip_masks[i])
                cnt += 1
        # 모든 면이 H(0) 또는 T(1)인지 확인
        if state == 0 or state == (1 << 9) - 1:
            min_op = min(min_op, cnt)
    return min_op if min_op != float('inf') else -1

# 입력 처리
T = int(input())
for _ in range(T):
    board = [input().split() for _ in range(3)]
    state = coin_to_bit(board)
    print(min_operations(state))
