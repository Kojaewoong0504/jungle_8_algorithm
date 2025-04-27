n = int(input())

bin_data = str(bin(n))[2:]
bin_data = bin_data[::-1]
result = 0
for i in range(len(bin_data)):
    if bin_data[i] == "1":
        result += (3**i)
print(result)
