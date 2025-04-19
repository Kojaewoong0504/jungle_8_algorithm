s = input()

zero_count = 0
one_count = 0

memory = s[0]

for i in range(1, len(s)):
    if memory != s[i]:
        if memory == "0":
            zero_count += 1
            memory = s[i]
        else:
            one_count += 1
            memory = s[i]
if memory == "0":
    zero_count += 1
else:
    one_count += 1

print(min(zero_count, one_count))