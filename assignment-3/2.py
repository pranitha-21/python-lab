T=int(input("Enter no. of test cases:"))
print("Enter Numbers:")
l=[]
for i in range(T):
    a=int(input())
    l.append(a)
i=0
k=1
f=[0]
while max(l)>i:
    b=i
    i=k
    k=k+b
    f.append(i)
for i in range(T):
    if l[i] in f:
        print("{l[i]} IsFibo")
    else:
        print(f"{l[i]} IsnotFibo")