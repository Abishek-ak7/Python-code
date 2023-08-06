a=list(map(str,input().split()))
k=[]
o=0
for i in a:
    t,r=i.split(":")
    t=int(t)
    r=int(r)
    if t>10:
        o+=1
    elif t==10 and t+r>10:
        o+=1
    elif t<10:
        pass
print(o)
        
    
