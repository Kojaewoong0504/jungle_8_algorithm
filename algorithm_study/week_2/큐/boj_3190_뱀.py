from collections import deque

n = int(input())
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
directions = []

for _ in range(l):
    x, c = input().split()
    directions.append((int(x), c))

board = [[0 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

# 사과 위치 표시
for apple in apples:
    x, y = apple
    board[x-1][y-1] = 1

def game():
    # 뱀의 초기 위치와 방향 설정
    q = deque([(0, 0)])  # 뱀의 몸 좌표를 저장하는 큐
    visited[0][0] = True  # 뱀이 있는 위치 표시
    direction = 0  # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    time = 0
    dir_index = 0

    while True:
        time += 1
        head_x, head_y = q[-1]
        nx, ny = head_x + dx[direction], head_y + dy[direction]

        # 벽이나 자기 자신과 충돌하는지 확인
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
            return time

        # 뱀 머리 이동
        q.append((nx, ny))
        visited[nx][ny] = True

        # 사과를 먹었는지 확인
        if board[nx][ny] == 1:
            board[nx][ny] = 0  # 사과 제거
        else:
            # 사과가 없으면 꼬리 제거
            tail_x, tail_y = q.popleft()
            visited[tail_x][tail_y] = False

        # 방향 전환 확인
        if dir_index < len(directions) and time == directions[dir_index][0]:
            if directions[dir_index][1] == 'L':
                direction = (direction - 1) % 4
            else:  # 'D'
                direction = (direction + 1) % 4
            dir_index += 1

# 게임 실행 및 결과 출력
print(game())
