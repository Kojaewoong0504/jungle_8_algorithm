import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

one, two = set(), set()
ans = 0

for a in arr:
    is_good = False
    # 판정: A[i] = s + (p+q)  <=>  A[i]-s in two
    for s in one:
        if (a - s) in two:
            is_good = True
            break
    if is_good:
        ans += 1

    # 갱신 (현재 a는 다음 원소 판정부터 사용)
    # 먼저 one에 넣고, one의 모든 s에 대해 a+s를 two에 추가
    one.add(a)
    for s in one:
        two.add(a + s)

print(ans)
