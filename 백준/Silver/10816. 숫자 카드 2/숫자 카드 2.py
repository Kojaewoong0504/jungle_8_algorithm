n = int(input())
n_lsit = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_dict = {}
for i in n_lsit:
    if i in n_dict:
        n_dict[i] += 1
    else:
        n_dict[i] = 1

for j in m_list:
    if j in n_dict:
        print(n_dict[j], end=' ')
    else:
        print(0, end=' ')
        