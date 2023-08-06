n=int(input())
l=[]
def avg(
for i in range(n):
    l.append(int(input()))   
sum=0
for i in l:
    sum+=i
avg=(sum/n)
print("%.2f"%(avg))
