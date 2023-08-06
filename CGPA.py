a=input("Enter maths grade: ")
b=input("Enter english grade: ")
c=input("Enter adp grade: ")
d=input("Enter pdsc grade: ")
e=input("Enter dpco grade: ")
f=input("Enter EG grade: ")
g=input("Enter aptitude grade: ")

if a=='A+' or a=='a+':
    mark1=9
elif a=='A' or a=='a':
    mark1=8
elif a=='B+' or a=='b+':
    mark1=7
elif a=='B' or a=='c':
    mark1=6
elif a=='O' or a=='o':
    mark1=10

if b=='A+' or b=='a+':
    mark2=9
elif b=='A' or b=='a':
    mark2=8
elif b=='B+' or b=='b+':
    mark2=7
elif b=='B' or b=='c':
    mark2=6
elif b=='O' or b=='o':
    mark2=10

if c=='A+' or c=='a+':
    mark3=9
elif c=='A' or c=='a':
    mark3=8
elif c=='B+' or c=='b+':
    mark3=7
elif c=='B' or c=='c':
    mark3=6
elif c=='O' or c=='o':
    mark3=10

if d=='A+' or d=='a+':
    mark4=9
elif d=='A' or d=='a':
    mark4=8
elif d=='B+' or d=='b+':
    mark4=7
elif d=='B' or d=='c':
    mark4=6
elif d=='O' or d=='o':
    mark4=10

if e=='A+' or e=='a+':
    mark5=9
elif e=='A' or e=='a':
    mark5=8
elif e=='B+' or e=='b+':
    mark5=7
elif e=='B' or e=='c':
    mark5=6
elif e=='O' or e=='o':
    mark5=10


if f=='A+' or f=='a+':
    mark6=9
elif f=='A' or f=='a':
    mark6=8
elif f=='B+' or f=='b+':
    mark6=7
elif f=='B' or f=='c':
    mark6=6
elif f=='O' or f=='o':
    mark6=10

if g=='A+' or g=='a+':
    mark7=9
elif g=='A' or g=='a':
    mark7=8
elif g=='B+' or g=='b+':
    mark7=7
elif g=='B' or g=='c':
    mark7=6
elif g=='O' or g=='o':
    mark7=10

mc=4
ec=3
adpc=4
pdscc=3
dpcoc=3
egc=2
aptc=1

park1=mark1*mc
park2=mark2*ec
park3=mark3*adpc
park4=mark4*pdscc
park5=mark5*dpcoc
park6=mark6*egc
park7=mark7*aptc
print(park1+park2+park3+park4+park5+park6+park7)
gpa=(park1+park2+park3+park4+park5+park6+park7)/20
print("Gpa for second yr = ",gpa)
l=float(input("ENter 1st sem gpa: "))
print("CGPA= ",((l*24)+(gpa*20))/44)
