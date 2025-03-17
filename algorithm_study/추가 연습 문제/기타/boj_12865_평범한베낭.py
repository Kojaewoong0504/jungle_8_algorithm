import heapq

n, k = map(int, input().split())

item_list = []

for _ in range(n):
    item_list.append(list(map(int,input().split())))

item_list.sort()

print(item_list)