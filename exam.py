a=list(map(int,input().split()))
g=[]
for i in a:
    if a.count(i)>1:
        g.append(i)
print(*list(set(g)))

