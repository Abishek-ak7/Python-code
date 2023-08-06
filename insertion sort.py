n=int(input())
l=[]
for i in range(0,n):
    l.append(int(input()))
for i in range(1,n):
    j=i
    while j>0 and l[j-1]>l[j]:
        temp=l[j]
        l[j]=l[j-1]
        l[j-1]=temp
        j-=1
print(l)
