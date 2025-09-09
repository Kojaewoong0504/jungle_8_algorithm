from collections import deque
import sys
input = sys.stdin.readline

# 세그먼트 비트 (a=0 ... g=6)
A,B,C,D,E,F,G = [1<<i for i in range(7)]
mask = {
    '0': A|B|C|D|E|F,
    '1': B|C,
    '2': A|B|D|E|G,
    '3': A|B|C|D|G,
    '4': B|C|F|G,
    '5': A|C|D|F|G,
    '6': A|C|D|E|F|G,
    '7': A|B|C,
    '8': A|B|C|D|E|F|G,
    '9': A|B|C|D|F|G,
}

N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]
need = [[mask[ch] for ch in row] for row in grid]

def can_right(x,y):  # (x,y) -> (x,y+1)
    left = need[x][y]; right = need[x][y+1]
    return ((left & B) and (right & F)) or ((left & C) and (right & E))

def can_down(x,y):   # (x,y) -> (x+1,y)
    up = need[x][y]; down = need[x+1][y]
    return (up & D) and (down & A)

vis = [[False]*M for _ in range(N)]
q = deque([(0,0)])
vis[0][0] = True
cnt = 1

while q:
    x,y = q.popleft()
    # 좌우
    if y+1 < M and not vis[x][y+1] and can_right(x,y):
        vis[x][y+1]=True; q.append((x,y+1)); cnt+=1
    if y-1 >= 0 and not vis[x][y-1] and can_right(x,y-1):
        vis[x][y-1]=True; q.append((x,y-1)); cnt+=1
    # 상하
    if x+1 < N and not vis[x+1][y] and can_down(x,y):
        vis[x+1][y]=True; q.append((x+1,y)); cnt+=1
    if x-1 >= 0 and not vis[x-1][y] and can_down(x-1,y):
        vis[x-1][y]=True; q.append((x-1,y)); cnt+=1

print("YES" if cnt == N*M else "NO")