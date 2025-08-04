N  =  int(input().rstrip())
tot  =  0
idx  =  1
while  1:
    if ((N+1)*idx)//N  >=  N:
        print(tot)
        break
    else:
        tot  += ((N+1)*idx)
    idx  +=  1