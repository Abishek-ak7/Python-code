n=int(input())
l=[]
for i in range(0,n):
    l.append(int(input()))
for i in range(0,n-1):
    for j in range(i+1,n):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)
    
