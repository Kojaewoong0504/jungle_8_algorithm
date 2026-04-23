puzzle = ['ABCD', 'EFGH', 'IJKL', 'MNO.']
puzzle2 = []  # 현재 퍼즐 상태
pos = {}  # 흩어진 퍼즐의 이름과 위치
cnt = 0  # 흩어짐 정도
for _ in range(4):
    puzzle2.append(input())

# 흩어진 퍼즐의 이름과 위치 저장
for i in range(4):
    for j in range(4):
        if puzzle[i][j] != puzzle2[i][j] and puzzle2[i][j] != '.':
            pos[puzzle2[i][j]] = (i, j)

# 흩어진 위치와 원래 위치의 거리 비교
for i in range(4):
    for j in range(4):
        if puzzle[i][j] in pos.keys():
            cnt += abs(pos[puzzle[i][j]][0]-i) + abs(pos[puzzle[i][j]][1]-j)

print(cnt)