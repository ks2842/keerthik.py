p,k=map(int,input().split())
for g in range(p+1,k):
    z=0
    m=g
    while m>0:
       a=m%10
       m=m//10
       b=a**3
       z=z+b
    if(g==z):
       print(z,end=' ')
