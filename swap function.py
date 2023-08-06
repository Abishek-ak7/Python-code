def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    print("After swap a=",a,"b=",b)
a=int(input())
b=int(input())
print("Before swap a=",a,"b=",b)
swap(a,b)
