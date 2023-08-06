























n=int(input())
l,s=[],0
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if (i==0 and j==0)or(i==0 and j==n-1)or(i==n-1 and j==0)or(i==n-1 and j==n-1):
            s=s+l[i][j]
print(s)







































