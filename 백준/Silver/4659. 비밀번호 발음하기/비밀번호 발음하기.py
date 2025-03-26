import re


def is_acceptable(password):
    # 모음이 있는지 확인
    if not re.search(r'[aeiou]', password):
        return False

    # 모음 3개 또는 자음 3개 연속 확인
    if re.search(r'[aeiou]{3}|[^aeiou]{3}', password):
        return False

    # 같은 글자 연속 확인 (ee, oo 제외)
    if re.search(r'([^eo])\1|e{2}e+|o{2}o+', password):
        return False

    return True


while True:
    data = input()
    if data == "end":
        exit(0)
    if is_acceptable(data):
        print(f"<{data}> is acceptable.")
    else:
        print(f"<{data}> is not acceptable.")