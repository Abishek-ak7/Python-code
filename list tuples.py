n=int(input("Enter the size of the list : "))
list=[]
print("Enter the book details :")
for i in range(n):
    list.append(input())
print(list)
print('list operations')
print('\n1.append\n2.extend\n3.insert\n4.remove\n5.pop\n6.slice\n7.reverse\n8.length\n9.sort\n')
while(True):
    c=int(input("Enter your choice :"))
    if (c==1):
        list.append("C")
        list.append("C++")
        print(list)
    elif (c==2):
        list.extend(["DMBS","AI","ML"])
        print(list)
    elif (c==3):
        list.insert(3,"DS")
        list.insert(4,"eng")
        print(list)
    elif (c==4):
        list.remove("eng")
        print(list)
    elif (c==5):
        list.pop()
        list.pop(5)
        print(list)
    elif (c==6):
        list[2:5]
        print(list)
    elif (c==7):
        list.reverse()
        print(list)
    elif (c==8):
        len(list)
        print(list)
    elif (c==9):
        list.sort()
        print(list)
    else:
        print("Invalid choice")
        break
