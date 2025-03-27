import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def find_tree(start, end):
    if start > end:
        return

    root = trees[start]
    idx = start + 1
    while idx <= end and trees[idx] < root:
        idx += 1

    find_tree(start + 1, idx - 1)
    find_tree(idx, end)
    print(root)

# 입력 처리
trees = []
while True:
    try:
        trees.append(int(input()))
    except:
        break

# 후위 순회 결과 출력
find_tree(0, len(trees) - 1)
