n=int(input("Enter the size of the list :"))
sum=0
for num in range(2,n+1):
    i=2
    for i in range(2,num):
        if int(num%i)==0:
            i=num
            break
    if i is not num:
        sum +=num
print("\nsum of n prime numbers ",sum)
