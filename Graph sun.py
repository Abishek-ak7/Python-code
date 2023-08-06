height=[1,2,1]
k=max(height)
U=0
u=height.index(k)
for i in range(u,len(height)-1):
     U+=1
print(U*height[-1])    
