while True:
     try:
         mark = int(input("Enter the Mark: "))
         if mark >=0 and mark <=100:
            print("Valid Marks Range")
         else:
            print("Invalid Marks")
     except ValueError as err:
         print(err)
         break
