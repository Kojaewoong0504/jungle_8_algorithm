import sys
tc=int(sys.stdin.readline())
for k in range(tc):
    n=int(sys.stdin.readline())
    lst=[]
    for _ in range(n):
        s=list(map(int,sys.stdin.readline().split()))
        lst.append(s)
    lst.sort(key=lambda x:(x[0],x[2],x[1]))
    day=0
    time=-1
    count=0
    for i in range(n):
        if lst[i][0]>day:
            day=lst[i][0]
            time=lst[i][2]
            count+=1
        else:
            if lst[i][1]>=time:
                time=lst[i][2]
                count+=1
    print('Scenario #{}:'.format(k+1))
    print(count)
    print()