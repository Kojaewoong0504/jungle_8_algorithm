import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
card = deque(range(1, n+1))

while len(card) > 1:
    print(card.popleft(), end=" ")  # 제일 위의 카드를 버림 (O(1) 연산)
    card.append(card.popleft())  # 그 다음 카드를 맨 아래로 이동 (O(1) 연산)

print(card[0])
