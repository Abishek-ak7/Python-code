f1 = input("Enter Source File :")
f2 = input("Enter Destination File :")
fr = open(f1,'r')
fw = open(f2,'w')
for line in fr.readlines():
     fw.write(line)
fr.close()
fw.close()
print("File Copied Successfully")
