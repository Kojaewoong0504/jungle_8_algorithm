import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input())
w = list(map(int, input().split()))
S = sum(w)

seen = bytearray(S + 1)

def dfs(i, cur):
    if i == k:
        x = abs(cur)
        if x != 0:         # 물 무게는 양수만 카운트
            seen[x] = 1
        return
    g = w[i]
    dfs(i + 1, cur - g)    # 그릇과 같은 편
    dfs(i + 1, cur)        # 사용 안 함
    dfs(i + 1, cur + g)    # 그릇 반대편

dfs(0, 0)

possible = sum(seen[1:])
print(S - possible)