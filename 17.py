y=int(input())
k=0
p=y
while p>0:
   digit=p%10
   k+=digit**3
   p//10
if y==k:
   print("yes")
else:
   print("no")
