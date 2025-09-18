import sys
from collections import defaultdict
input = sys.stdin.readline
n, m = map(int, input().split())

words = defaultdict(int)

for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        words[word] += 1
data = words.items()
sorted_words = sorted(data, key= lambda x: (-x[1], -len(x[0]), x[0]))

for word, count in sorted_words:
    print(word)
