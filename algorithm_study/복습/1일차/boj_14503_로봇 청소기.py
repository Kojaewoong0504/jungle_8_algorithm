n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0

while True:
    # 1. 현재 칸이 청소되지 않았으면 청소
    if room[r][c] == 0:
        room[r][c] = 2  # 청소한 곳은 2로 표시
        cnt += 1

    cleaned = False
    for _ in range(4):
        # 2. 왼쪽 방향으로 회전
        d = (d + 3) % 4
        nr, nc = r + dr[d], c + dc[d]

        # 앞쪽 칸이 청소되지 않은 빈 칸이면 이동
        if room[nr][nc] == 0:
            r, c = nr, nc
            cleaned = True
            break

    if not cleaned:
        # 3. 네 방향 모두 청소됨 → 뒤로 갈 수 있는지 확인
        back_d = (d + 2) % 4
        br, bc = r + dr[back_d], c + dc[back_d]
        if room[br][bc] == 1:
            break  # 뒤가 벽이면 종료
        else:
            r, c = br, bc  # 후진
print(cnt)
