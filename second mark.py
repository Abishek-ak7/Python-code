a=int(input())
b=[]
k=[]
for i in range(a):
    b.append(input())
    k.append(float(input()))
g=min(k)
q=k.index(g)
b.pop(q)
t=[]
for i in k:
    if i==g:
        continue
    else:
        t.append(i)
d=min(t)
z=[]
if t.count(d)>1:
    v=t.index(d)
    z.append(b[v])
    t.pop(v)
    b.pop(v)
    x=min(t)
    m=t.index(x)
    z.append(b[m])
    z.sort()
    for i in z:
        print(i)
else:
    v=t.index(d)
    z.append(b[v])
    for i in z:
        print(i)
    

    
