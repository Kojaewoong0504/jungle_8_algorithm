n, m = map(int, input().split())

bin_list = []

for _ in range(n):
    data = input().split(" ")[1]
    bin_data = ''.join(['1' if c == 'Y' else '0' for c in data])
    bin_list.append(int(bin_data, 2))

max_song = 0
min_guitar = float("INF")
for i in range(1, 1 << n):
    cal_data = 0
    for j in range(n):
        if i & (1 << j):
            cal_data |= bin_list[j]

    song_count = bin(cal_data).count('1')
    if song_count > max_song:
        max_song = song_count
        min_guitar = bin(i).count('1')
    elif song_count == max_song:
        min_guitar = min(min_guitar, bin(i).count('1'))

if max_song == 0:
    print(-1)
else:
    print(min_guitar)
