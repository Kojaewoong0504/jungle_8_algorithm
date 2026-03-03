import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))

sum_cards = sum(cards)

heapq.heapify(cards)

for _ in range(m):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    card_sum = a + b
    heapq.heappush(cards, card_sum)
    heapq.heappush(cards, card_sum)

print(sum(cards))