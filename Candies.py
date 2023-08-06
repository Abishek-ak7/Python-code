candies=list(map(int,input().split()))
extraCandies=int(input())
u=max(candies)
k=[]
for i in candies:
    if i + extraCandies >= u:
        k.append("true")
    else:
        k.append("false")
print(k)
