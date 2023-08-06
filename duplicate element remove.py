n=int(input("enter the size of the list :"))
list=[]
for i in range(n):
    list.append(int(input()))
nlist=[]
for i in list:
    if i not in nlist:
        nlist.append(i)
print(nlist)
