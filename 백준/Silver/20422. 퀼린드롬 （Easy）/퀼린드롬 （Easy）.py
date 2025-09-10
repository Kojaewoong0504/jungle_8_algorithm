import sys

def make_map():
    m = {}
    m['A'] = 'A'
    m['E'] = '3'
    m['3'] = 'E'
    m['H'] = 'H'
    m['I'] = 'I'
    m['M'] = 'M'
    m['O'] = 'O'
    m['S'] = '2'
    m['2'] = 'S'
    m['T'] = 'T'
    m['U'] = 'U'
    m['V'] = 'V'
    m['W'] = 'W'
    m['X'] = 'X'
    m['Y'] = 'Y'
    m['Z'] = '5'
    m['5'] = 'Z'
    m['b'] = 'd'
    m['d'] = 'b'
    m['i'] = 'i'
    m['l'] = 'l'
    m['m'] = 'm'
    m['n'] = 'n'
    m['o'] = 'o'
    m['p'] = 'q'
    m['q'] = 'p'
    m['r'] = '7'
    m['7'] = 'r'
    m['u'] = 'u'
    m['v'] = 'v'
    m['w'] = 'w'
    m['x'] = 'x'
    m['0'] = '0'
    m['1'] = '1'
    m['8'] = '8'
    return m

def is_small_alpha(c: str) -> bool:
    return 'a' <= c <= 'z'

def is_big_alpha(c: str) -> bool:
    return 'A' <= c <= 'Z'

def main():
    s = sys.stdin.readline().strip()
    m = make_map()
    n = len(s)

    # 왼쪽 절반과 오른쪽 절반(거울쪽) 결과를 따로 모은 뒤 이어 붙임
    left_part = []
    right_part = []  # C++은 앞에 붙였지만, 우리는 모아두고 마지막에 뒤집어서 붙임

    avail = True
    for i in range((n + 1) // 2):
        l = s[i]
        r = s[n - 1 - i]

        # 왼쪽/오른쪽 후보 (원문 + 대소문자 바꾼 것)
        ll = [l]
        if is_small_alpha(l):
            ll.append(l.upper())
        elif is_big_alpha(l):
            ll.append(l.lower())

        rr = [r]
        if is_small_alpha(r):
            rr.append(r.upper())
        elif is_big_alpha(r):
            rr.append(r.lower())

        matched = False
        for c in ll:
            if c in m:
                cc = m[c]
                # 오른쪽 후보 중에 cc와 일치하는 게 있으면 매칭
                if cc in rr:
                    matched = True
                    left_part.append(c)
                    # 가운데가 아니면 오른쪽 파트에도 대응 문자 추가
                    if i != n - 1 - i:
                        right_part.append(cc)
                    break
        if not matched:
            avail = False
            break

    if not avail:
        print(-1)
    else:
        # right_part는 C++에서 앞에 붙였던 것을 뒤집어서 붙이면 동일
        print(''.join(left_part) + ''.join(reversed(right_part)))

if __name__ == "__main__":
    main()
