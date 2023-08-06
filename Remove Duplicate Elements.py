n=int(input("Enter the size of list:"))
lst=[]
print("Enter the elements:")
for i in range(0,n):
    lst.append(input())
print("The elements in the list are:")
non_dup=[]
uniq=set()
for element in lst:
     if element not in uniq:
        non_dup.append(element)
        uniq.add(element)
print("The unique elements in the list are:",non_dup)
