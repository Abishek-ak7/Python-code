x=int(input())
y=list(map(int,input().split()))
z=[]
for i in range(x):
    s=y[-(i+1)]%10
    a=y[i]*s
    print(a,end=" ")
