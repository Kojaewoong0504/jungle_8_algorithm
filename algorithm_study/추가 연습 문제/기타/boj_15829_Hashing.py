# v1

n = int(input())
input_data = list(input())
trans_num = 0

for i in range(n):
    data1 = ord(input_data[i])-96
    data2 = (data1 * (31 ** i)) % 1234567891
    trans_num += data2

print(trans_num)

# v2
n = int(input())
input_data = list(input())
trans_num = 0
mod = 1234567891

for i in range(n):
    data1 = ord(input_data[i])-96
    data2 = (data1 * pow(31, i, mod)) % mod
    trans_num = (trans_num + data2) % mod

print(trans_num)

# v3
n = int(input())
input_data = list(input())
trans_num = 0
mod = 1234567891

for i in range(n):
    data1 = ord(input_data[i])-96
    data2 = (data1 * (31 ** i)) % mod
    trans_num = (trans_num + data2) % mod

print(trans_num)