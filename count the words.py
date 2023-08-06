f=open("AK.txt","r")
cl=cc=cw=0
for line in f:
    words=line.split()
    cl+=1
    cw+=len(words)
    cc+=len(line)
f.close()
print("No of lines:",cl)
print("No of characters:",cc)
print("No of words:",cw)
    
