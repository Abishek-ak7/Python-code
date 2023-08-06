a=int(input())
b=0
c=1
print(b,end=" ")
print(c,end=" ")
for i in range(a):
    g=b+c
    print(g,end=" ")
    b=c
    c=g
    
