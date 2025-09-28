import sys

def main():
    input = sys.stdin.readline
    A, B = map(int, input().split())
    m = int(input())
    digits = list(map(int, input().split()))  # 높은 자릿수 → 낮은 자릿수

    # A진수 → 10진수
    value = 0
    for d in digits:
        value = value * A + d

    # 10진수 → B진수 (값이 양수라고 했지만 혹시 몰라 0 처리)
    if value == 0:
        print(0)
        return

    out = []
    while value > 0:
        out.append(value % B)
        value //= B
    out.reverse()

    print(*out)

if __name__ == "__main__":
    main()
