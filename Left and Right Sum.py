nums=[10,4,8,3]
U=[]
J=nums[::-1]
D=[]
L=[]
k=0
u=0
U.append(0)
D.append(0)
print(J)
for i in range(0,len(nums)-1):
     k+=nums[i]
     U.append(k)
print(U)
for i in range(len(nums)-1):
    u+=J[i]
    D.append(u)
print(D)
D.reverse()
for i in range(len(nums)):
    t=U[i]-D[i]
    if t<0:
        t=-1*t
        L.append(t)
    else:
        L.append(t)
print(L)
