f1=input()
f2=input()
fr=open(f1,"r")
fw=open(f2,"w")
for line in fr.readlines():
    fw.write(line)
fr.close()
fw.close()
print("File Succesfully Copied")
