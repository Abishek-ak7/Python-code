n=int(input("enter the size of the list :"))
list=[]
for i in range(n):
    list.append(int(input()))
smallest=largest=list[0]
for i in range(1,n):
    if smallest>list[i]:
        smallest=list[i]
    elif largest<list[i]:
        largest=list[i]
print("Minimum element in list :",smallest)
print("Maximum element in list :",largest)
