def sum(n):
    c=0
    while n>0:
        d=n%10
        c+=d
        n//=10
    print(c)

n=int(input())
sum(n)
