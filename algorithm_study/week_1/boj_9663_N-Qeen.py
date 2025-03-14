n = int(input())

queen = [-1] * n

def is_able_attack(row, col):
    for i in range(row):
        if queen[i] == col:
            return False
        if abs(row - i) == abs(col- queen[i]):
            return False
    return True

def recursion(n, row):
    count = 0
    # 탈출 조건
    if row == n:
        return 1

    for col in range(n):
        # 퀸이 공격 가능한지 검사 반환값 == bool
        # 만약 공격 가능하다 판단되면 pass
        # 공격 불가인 경우 재귀 함수로 다음 퀸 배치
        if is_able_attack(row, col):
            queen[row] = col
            count += recursion(n, row+1)
    return count

print(recursion(n, 0))

