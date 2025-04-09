string_data = input()


left = 1
right = len(string_data)

z_count = 0
o_count = 0
tmp = string_data[0]
while left < right:
    data = string_data[left]
    if tmp != data:
        if tmp == "0":
            z_count += 1
        else:
            o_count += 1
    tmp = data
    left += 1

if string_data[-1] == "0":
    z_count += 1
else:
    o_count += 1

print(min(z_count,o_count))