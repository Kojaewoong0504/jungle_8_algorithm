import copy

R, C = map(int, input().split())

card = []
for _ in range(R):
    card.append(list(input()))

A, B = map(int, input().split())

# 오른쪽 위 부분 대칭
for i in range(R):
    row = []
    for j in range(C - 1, -1, -1):
        row.append(card[i][j])
    card[i].extend(row)

# 아래 부분 대칭
for i in range(R - 1, -1, -1):
    row = copy.deepcopy(card[i])  # 깊은 복사
    card.append(row)

# 에러 처리
if card[A - 1][B - 1] == '#':
    card[A - 1][B - 1] = '.'
else:
    card[A - 1][B - 1] = '#'

for c in card:
    print(''.join(c))