f1=input("Enter the source file :")
f2=input("Enter the destination file :")
fr=open(f1,"r")
fw=open(f2,"w")
for line in fr.readlines():
    fw.write(line)
fr.close()
fw.close()
print("File copied successfully ")
