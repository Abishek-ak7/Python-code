n=int(input("Enter the size of the list :"))
list=[]
flag=False
for i in range(0,n):
    list.append(int(input()))
print(list)
x=int(input("Enter the element to be found :"))
for i in range(0,n):
    if x==list[i]:
        flag=True
if flag==True:
    print("Element is found ")
else:
    print("Element is not found ") 
