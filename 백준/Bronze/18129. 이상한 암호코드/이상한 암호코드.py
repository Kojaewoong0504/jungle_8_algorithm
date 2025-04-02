strange, k = input().split()
k = int(k)
strange = strange.upper()

result = ""
processed_chars = set()  # 이미 처리된 문자들을 저장
i = 0

while i < len(strange):
    char = strange[i]
    count = 1

    # 같은 문자가 연속으로 나오는 개수 세기
    j = i + 1
    while j < len(strange) and strange[j] == char:
        count += 1
        j += 1

    # 이미 처리된 문자인지 확인
    if char in processed_chars:
        # 이미 처리된 문자면 건너뛰기
        i = j
        continue

    # 처리되지 않은 문자면 결과에 추가하고 처리된 문자로 표시
    processed_chars.add(char)

    if count >= k:
        result += "1"
    else:
        result += "0"

    i = j

print(result)
