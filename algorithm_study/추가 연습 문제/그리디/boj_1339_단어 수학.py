from collections import defaultdict

n = int(input())
words = [input().strip() for _ in range(n)]

weight = defaultdict(int)

# 1) 글자별 가중치 누적
for w in words:
    power = 0
    for ch in w[::-1]:          # 오른쪽(일의 자리)부터
        weight[ch] += 10 ** power
        power += 1

# 2) 가중치 큰 순으로 정렬 후 9부터 배정
sorted_letters = sorted(weight.items(), key=lambda x: -x[1])
digit_map = {}
digit = 9
for ch, _ in sorted_letters:
    digit_map[ch] = str(digit)
    digit -= 1

# 3) 치환 후 합계
total = 0
for w in words:
    num = int(''.join(digit_map[ch] for ch in w))
    total += num

print(total)
