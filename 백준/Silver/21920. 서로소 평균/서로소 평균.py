import sys
input=sys.stdin.readline

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return (a*b)//gcd(a,b)

n=int(input().rstrip())
a=list(map(int,input().split())) 
x=int(input().rstrip())  

mean=[]
for i in range(n):
    if a[i]!=x: 
        if gcd(a[i],x)==1:
            mean.append(a[i])

print('{:.6f}'.format(sum(mean)/len(mean))) 