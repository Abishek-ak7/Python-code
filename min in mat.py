a,b=map(int,input().split())
mat=[]
for i in range(a):
    mat.append(list(map(int,input().split())))
    mat[i].remove(min(mat[i]))
print(mat)
mat=[[mat[j][i] for j in range(len(mat))]for i in range(len(mat[0]))]
for i in mat:
    i.remove(min(i))
tran=[[mat[j][i] for j in range(len(mat))]for i in range(len(mat[0]))]
for i in tran:
    print(*i)
