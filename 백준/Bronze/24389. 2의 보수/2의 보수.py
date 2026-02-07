binary = int(input())
length = 32 - len(bin(binary)[2:])
initial = length*'0' + bin(binary)[2:]
tmp_lst = list(length*'0' + bin(binary)[2:])
 
for i in range(len(tmp_lst)) :
    if tmp_lst[i] == '0' :
        tmp_lst[i] = '1'
    else :
        tmp_lst[i] = '0'
 
result = bin(int(''.join(tmp_lst), 2) + 1)[2:]
 
cnt = 0
for i in range(32) :
    if initial[i] != result[i] :
        cnt += 1
 
print(cnt)