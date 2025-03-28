import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(r,c):
    visited[r][c] = True
    cnt = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not visited[nr][nc]:
            cnt += dfs(nr,nc)
    return cnt

n,m = map(int,input().split())
earth = [list(map(int,input().split())) for _ in range(n)]
visited = [[True]*m for _ in range(n)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
ice_list = []

# 행열을 돌며 0(바다)가 아닌 빙산의 좌표와 빙산의 높이를 기록
for i in range(n):
    for j in range(m):
        if earth[i][j]>0:
            ice_list.append((i,j,earth[i][j]))

for year in range(1, 1001): # 1년 부터 최대 1000년 까지 반복
    for i in range(len(ice_list)):
        r,c,h = ice_list[i]
        for j in range(4): #4방향에 대해서 빙산이 바다와 접했는지 확인
            nr = r + dr[j]
            nc = c + dc[j]
            if earth[nr][nc] == 0:
                h -= 1
        ice_list[i] = (r,c,h)

    i = 0
    while i < len(ice_list):
        r,c,h = ice_list[i]
        if h <= 0: #빙사의 높이가 0보다 작거나 같아진 경우
            earth[r][c] = 0
            ice_list[i] = ice_list[-1]
            ice_list.pop()
        else:
            visited[r][c] = False
            i += 1
    if len(ice_list) != 0:
        if dfs(ice_list[0][0], ice_list[0][1]) != len(ice_list):
            print(year)
            break
    else:
        print(0)
        break