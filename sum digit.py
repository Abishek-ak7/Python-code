n=int(input())
sum=0
while n>0:
    a=n%10
    sum+=a
    n//=10
print(sum)
