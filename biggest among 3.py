a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=int(input("Enter the third number :"))
if a>b and a>c:
    largest=a
elif b>c:
    largest=b
else:
    largest=c
print("Biggest among three numbers :",largest)
