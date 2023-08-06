n=int(input('Enter the size of the list:'))
lst=[]
print("Enter the Book details:")
for i in range(n):
    lst.append(input())
print(lst)
print('List operations')
print('1.append \n 2.extend \n3.insert \n4.remove\n 5.pop\n 6.Slice \n 7.Reverse\n 8.length\n 9.sort\n')
while(True):
    c=int(input('Enter your Choice:'))
    if(c==1):
        lst.append("C")
        lst.append("C++")
        print(lst)
    elif(c==2):
         lst.extend(["DBMS","AI","ML"])
         print(lst)
    elif(c==3):
        lst.insert(3,"DS")
        lst.insert(4,"eng")
        print(lst)
    elif(c==4):
        lst.remove("eng")
        print(lst)
    elif(c==5):
        lst.pop()
        lst.pop(5)
        print(lst)
    elif(c==6):
        lst=lst[2:5]
        print(lst)
    elif(c==7):
        lst.reverse()
        print(lst)
    elif(c==8):
        st=len(lst)
        print(st)
    elif(c==9):
        lst.sort()
        print(lst)
    else:
        print("Invalid choice")
        break
tup=(10,50,30,40,20)
print (len(tup))
print ('max of Tup', max(tup))
print ('min of Tup', min(tup))
print ('sum of Tup', sum(tup))
print ('Tup in sorted order', sorted(tup))

