k=int(input())
z=0
if k<=1000:
   for i in range(2,k):
       if(k%i==0):
          z=z+1
   if(z<=0):
       print("yes")
   else:
       print("no")
