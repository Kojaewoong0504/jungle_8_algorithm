import sys
input = sys.stdin.readline

n, q = map(int, input().split())
s = list(input().strip())

for _ in range(q):

    q_type, l, r = map(int, input().split())
    l -= 1
    r -= 1
    if q_type == 1:
        cnt = 1
        for i in range(l + 1, r + 1):
            if s[i] != s[i-1]:
                cnt += 1
        print(cnt)
    else:
        for i in range(l, r + 1):
            s[i] = chr((ord(s[i]) - ord('A') + 1) % 26 + ord('A'))