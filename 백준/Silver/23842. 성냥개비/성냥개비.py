import sys

cost_digit = [6,2,5,5,4,5,6,3,7,6]  # 0..9
def cost2(n):  # 두 자리 비용(leading zero)
    return cost_digit[n // 10] + cost_digit[n % 10]

def solve():
    N = int(sys.stdin.readline())
    # 빠른 컷
    if N < 16 or N > 46:
        print("impossible")
        return

    # 미리 두 자리 비용을 준비
    c2 = [cost2(i) for i in range(100)]

    # 00~99 완전탐색
    for x in range(100):
        for y in range(100):
            z = x + y
            if z > 99:   # 세 자리면 불가
                continue
            if c2[x] + c2[y] + c2[z] + 4 == N:  # +와 =가 각각 2개
                print(f"{x:02d}+{y:02d}={z:02d}")
                return
    print("impossible")

if __name__ == "__main__":
    solve()
