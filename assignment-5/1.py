L=int(input())
R=int(input())
a=[]
for i in range(L,R+1):
    for j in range(i,R+1):
        b=i^j
        a.append(b)
print(max(a))
