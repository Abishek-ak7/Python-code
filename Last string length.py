s=input()
k=list(s.split(" "))
print(k)
l=[]
for i in k:
    if i.isalnum():
        l.append(i)
print(l)
print(len(l[-1]))
