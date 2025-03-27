n = int(input())
have_list = list(map(int, input().split()))
m = int(input())
find_list = list(map(int, input().split()))

dict_data = {}
for i in range(n):
    dict_data[have_list[i]] = 0

for i in range(m):
    if find_list[i] in dict_data:
        print(1, end=' ')
    else:
        print(0, end=' ')