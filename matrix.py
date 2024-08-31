def Matr(n,m,v):
    if n <= 0 or m<=0:
        exit()
    matr=[]
    for i in range(n):
        matr.append([])
        for a in range(m):
            matr[i].append(v)
    print(matr)
f=int(input('n'))
f1=int(input('m'))
f2=int(input('v'))
Matr(f,f1,f2)

