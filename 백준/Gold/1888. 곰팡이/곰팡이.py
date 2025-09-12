from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()
 
h,w = map(int,input().split())
arr = [list(map(int,input())) for _ in range(h)]
dire = [(1,0),(0,1),(-1,0),(0,-1)]
inside = lambda x,y : 0<=x<w and 0<=y<h
 
def bfs(x,y,n): # 곰팡이 덩어리 BFS
    visit[y][x] = True
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for dx,dy in dire:
            nx,ny = x+dx,y+dy
            if inside(nx,ny) and not visit[ny][nx] and arr[ny][nx]:
                visit[ny][nx] = True
                q.append((nx,ny))
 
def check(): # 곰팡이 덩어리 개수 세는 함수
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] and not visit[i][j]:
                bfs(j,i,arr[i][j])
                cnt += 1
    return cnt      
 
def spread():
    narr = [[0]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            speed = arr[y][x]
            narr[y][x] = max(narr[y][x],arr[y][x])
            if speed:
                for nx in range(x-speed,x+speed+1):
                    for ny in range(y-speed,y+speed+1):
                        if inside(nx,ny) and arr[ny][nx] < arr[y][x]:
                            narr[ny][nx] = max(narr[ny][nx],arr[y][x])
    return narr
                
day = 0
visit = [[False]*w for _ in range(h)]
count = check()
while count > 1:
    visit = [[False]*w for _ in range(h)]
    arr = spread()
    count = check()
    day += 1
print(day)