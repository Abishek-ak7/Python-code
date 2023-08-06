def Sum(n):
    c=0
    while n>0:
        a=n%10
        c = c+a
        n=n//10
    return c
N,T=map(int,input().split())
sum=N
while T>0:
    sum = sum+Sum(sum)
    T=T-1
print(sum)
