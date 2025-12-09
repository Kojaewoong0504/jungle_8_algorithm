number_to_alpha = {i: chr(64 + i) for i in range(1, 27)}

while True:
    cell = input()
    if cell == "R0C0":
        break
    n, m = cell[1:cell.index('C')], int(cell[cell.index('C')+1:])
    result = []
    while m > 0:
        r = m % 26
        if r == 0:  
            result.append('Z')
            m = m // 26 - 1
        else:
            result.append(number_to_alpha[r])
            m //= 26
    print(''.join(reversed(result)) + str(n))