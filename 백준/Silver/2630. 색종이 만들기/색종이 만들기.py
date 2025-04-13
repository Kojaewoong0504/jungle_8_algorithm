n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white_count = 0  # 하얀색 색종이 개수
blue_count = 0  # 파란색 색종이 개수


def check_color(x, y, n):
    color = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                return False
    return True


def recursion(x, y, n):
    global white_count, blue_count

    # 현재 영역이 모두 같은 색인지 확인
    if check_color(x, y, n):
        if paper[x][y] == 0:
            white_count += 1  # 하얀색 색종이 추가
        else:
            blue_count += 1  # 파란색 색종이 추가
        return

    # 영역 분할
    half = n // 2
    recursion(x, y, half)  # 왼쪽 위
    recursion(x, y + half, half)  # 오른쪽 위
    recursion(x + half, y, half)  # 왼쪽 아래
    recursion(x + half, y + half, half)  # 오른쪽 아래


recursion(0, 0, n)
print(white_count)  # 하얀색 색종이 개수 출력
print(blue_count)  # 파란색 색종이 개수 출력
