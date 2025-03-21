import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))


def cut_tree(h):
    sum_data = []
    for i in trees:
        if i > h:
            sum_data.append(i-h)
    return sum(sum_data)

l, r = 0, max(trees)
while l <= r:
    mid = (l + r)//2
    if cut_tree(mid) >= m:
        l = mid + 1
    else:
        r = mid - 1

print(r)
