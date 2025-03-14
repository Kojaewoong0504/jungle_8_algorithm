arr = []
for i in range(9):
    arr.append(int(input()))

max_data = max(arr)
print(max_data)
print(arr.index(max_data) +1)