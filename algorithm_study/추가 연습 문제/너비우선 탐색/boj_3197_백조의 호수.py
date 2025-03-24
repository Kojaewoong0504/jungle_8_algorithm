from collections import deque


def solution(R, C, lake):
    # 방향 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 백조 위치 찾기
    swans = []
    water_q = deque()  # 현재 물 위치
    next_water_q = deque()  # 다음 날 녹을 얼음

    # 방문 체크 배열
    visited = [[False] * C for _ in range(R)]

    # 초기 상태 설정
    for i in range(R):
        for j in range(C):
            if lake[i][j] == 'L':
                swans.append((i, j))
                water_q.append((i, j))
                lake[i] = lake[i][:j] + '.' + lake[i][j + 1:]  # 백조 위치도 물로 변경
            if lake[i][j] == '.':
                water_q.append((i, j))

    # 백조 BFS 큐
    swan_q = deque([swans[0]])  # 첫 번째 백조 위치
    next_swan_q = deque()

    # 백조 방문 체크
    swan_visited = [[False] * C for _ in range(R)]
    swan_visited[swans[0][0]][swans[0][1]] = True

    day = 0

    while True:
        # 백조가 만날 수 있는지 확인
        while swan_q:
            x, y = swan_q.popleft()

            if x == swans[1][0] and y == swans[1][1]:  # 두 번째 백조를 만남
                return day

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < R and 0 <= ny < C and not swan_visited[nx][ny]:
                    swan_visited[nx][ny] = True

                    if lake[nx][ny] == '.':  # 물이면 현재 큐에 추가
                        swan_q.append((nx, ny))
                    else:  # 얼음이면 다음 큐에 추가
                        next_swan_q.append((nx, ny))

        # 하루가 지남
        day += 1

        # 얼음 녹이기
        while water_q:
            x, y = water_q.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                    if lake[nx][ny] == 'X':  # 얼음이면 녹임
                        lake[nx] = lake[nx][:ny] + '.' + lake[nx][ny + 1:]
                        visited[nx][ny] = True
                        next_water_q.append((nx, ny))

        # 큐 교체
        water_q = next_water_q
        next_water_q = deque()

        swan_q = next_swan_q
        next_swan_q = deque()

        if not swan_q:  # 더 이상 탐색할 곳이 없으면 불가능
            return -1


# 입력 처리
R, C = map(int, input().split())
lake = [input() for _ in range(R)]
print(solution(R, C, lake))
