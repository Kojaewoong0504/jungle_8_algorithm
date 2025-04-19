from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))


def bfs():
    q = deque([(0, 0)])  # (현재 금액, 사용한 동전 개수)
    visited = [False] * (k + 1)  # 방문 체크 배열
    visited[0] = True

    while q:
        curr_amount, coin_count = q.popleft()

        if curr_amount == k:
            return coin_count

        for coin in coins:
            next_amount = curr_amount + coin

            if next_amount <= k and not visited[next_amount]:
                visited[next_amount] = True
                q.append((next_amount, coin_count + 1))

    return -1  # 불가능한 경우


print(bfs())
