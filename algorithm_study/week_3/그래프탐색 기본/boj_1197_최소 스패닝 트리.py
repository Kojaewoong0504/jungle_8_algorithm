import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())
parent = [i for i in range(V + 1)]
tree = []
answer = 0

for _ in range(E):
    node1, node2, grade = map(int, input().split())
    tree.append([grade, node1, node2])
tree.sort()

for i in tree:
    grade, node1, node2 = i
    if find(node1) != find(node2):
        union(node1, node2)
        answer += grade

print(answer)