k=0
sub_string=input().strip()
string=input().strip()
for i in sub_string:
        if i in string:
            k+=1
if k==len(sub_string):
    print("1")
elif k>len(sub_string):
    if k%2==0:
        print(k//2)
    else:
        print(round(k/2))
else:
    if k%2==0:
        print(k//2)
    else:
        print(round(k/2))
