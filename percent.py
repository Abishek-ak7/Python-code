a=int(input())
h=[]
k=[]
q=[]
r=[]
w=0
for i in range(a):
    f=list(map(str,input().split()))
    r.append(f)
for i in range(len(r)):
    for o in r[i]:
        if o.isdigit():
            h.append(o)
            j=[eval(t) for t in h]
        else:
            k.append(o)
print(j)
z=list(j.split(", , ,"))
print(z)

for i in j:
    w+=i
q.append(w/3)
e=max(q)
p=q.index(e)
print(k[p])
print(k)
print(h)
print(q)

        
