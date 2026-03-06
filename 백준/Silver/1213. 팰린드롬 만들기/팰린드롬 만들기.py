name = input().strip()

count = [0] * 26
for ch in name:
    count[ord(ch) - ord('A')] += 1

# 홀수 개수 체크
odd_count = 0
odd_char = ""

for i in range(26):
    if count[i] % 2 == 1:
        odd_count += 1
        odd_char = chr(i + ord('A'))

if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    left = []

    # 왼쪽 절반 만들기
    for i in range(26):
        left.append(chr(i + ord('A')) * (count[i] // 2))

    left = "".join(left)
    right = left[::-1]

    # 가운데 문자 추가
    if odd_count == 1:
        print(left + odd_char + right)
    else:
        print(left + right)