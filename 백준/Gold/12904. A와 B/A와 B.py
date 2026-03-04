a = input()
b = input()

is_reverse = False

while len(b) > len(a):
    if not is_reverse:
        if b[-1] == 'A':
            b = b[:-1]
        else:
            b = b[:-1]
            is_reverse = True
    else:
        if b[0] == 'A':
            b = b[1:]
        else:
            b = b[1:]
            is_reverse = False

if not is_reverse:
    print(1 if a == b else 0)
else:
    print(1 if a == b[::-1] else 0)