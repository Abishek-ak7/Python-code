n=int(input("Enter the size of the list :"))
list=[]
for i in range(0,n):
    list.append(int(input()))
print(list)
x=int(input("Enter the element to be found :"))
low=0
high=n-1
mid=(low+high)//2
while low<=high:
    if x==list[mid]:
        print("Element is found")
        break
    elif list[mid]<x:
        low=mid+1
    else:
        high=mid-1
    mid=(low+high)//2
if low>high:
    print("Element is not found ")
