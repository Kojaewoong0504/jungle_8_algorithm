import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)

    a = 1
    while True:
        a *= 9
        if n <= a:
            print("Baekjoon wins.")
            break
        a *= 2
        if n <= a:
            print("Donghyuk wins.")
            break
