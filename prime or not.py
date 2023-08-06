n=int(input())
f=False
for i in range (1,n):
    for z in range(2,i):
       if i%z==0:
           f=True
           break
   
if f:
    print("NOT ")
else:
    print("Prime")

