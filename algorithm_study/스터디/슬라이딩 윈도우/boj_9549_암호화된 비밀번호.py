from collections import Counter

t = int(input())
for _ in range(t):
    encrypted = input()
    original = input()

    m = len(original)
    n = len(encrypted)

    if n < m:
        print("NO")
        continue

    target_counter = Counter(original)
    window_counter = Counter(encrypted[:m])

    found = False
    if window_counter == target_counter:
        found = True
    else:
        for i in range(m,n):
            left_char = encrypted[i - m]
            right_char = encrypted[i]
            window_counter[right_char] += 1
            window_counter[left_char] -= 1
            if window_counter[left_char] == 0:
                del window_counter[left_char]
            if window_counter == target_counter:
                found = True
                break

    print("YES" if found else "NO")
