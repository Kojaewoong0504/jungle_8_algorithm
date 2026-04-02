import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    students = [0] + list(map(int, input().split()))

    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    team_count = 0

    def dfs(x):
        global team_count
        visited[x] = True
        next_student = students[x]

        if not visited[next_student]:
            dfs(next_student)
        elif not finished[next_student]:
            # 사이클 발견
            cnt = 1
            cur = next_student
            while students[cur] != next_student:
                cur = students[cur]
                cnt += 1
            team_count += cnt

        finished[x] = True

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    print(n - team_count)