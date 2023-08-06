def palindrome(string):
     length = len(string)
     first = 0
     last = length -1
     status = 1
     while(first<last):
         if(string[first]==string[last]):
             first=first+1
             last=last-1
         else:
             status = 0
             break
     return int(status)
string = input("Enter the string: ")
status= palindrome(string)
if(status):
    print("It is a palindrome ")
else:
    print("Sorry! It is not a palindrome")
