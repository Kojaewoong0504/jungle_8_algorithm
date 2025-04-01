# 2차원 배열 초기화 (좌표가 1~100이므로 101x101 크기로 생성)
visited = [[False for _ in range(101)] for _ in range(101)]

# 각 직사각형에 대해
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    # 직사각형 내부의 모든 좌표를 방문 처리
    for x in range(x1, x2):
        for y in range(y1, y2):
            visited[x][y] = True

# 방문한 좌표의 개수 세기
area = 0
for x in range(1, 101):
    for y in range(1, 101):
        if visited[x][y]:
            area += 1

print(area)
