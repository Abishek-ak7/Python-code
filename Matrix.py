a = int(input())
for i in range(a):
    b,c=map(int,input().split())
    Y=[]
    for i in range(0,b):
        u=list(map(int,input().split()))
        Y.append(u)
    R=[]
    R.append(Y[0])
    print(Y)
    for i in range(1,len(Y)):
        if i%2 == 0:
            R.append(Y[i])
        else:
            r=Y[i][::-1]
            R.append(r)
    print(R)
    for i in R:
        print(*i,end= " ")

