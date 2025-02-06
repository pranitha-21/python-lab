T=int(input("Enter no. of test cases:"))
l=[]
height=1
for i in range(T):
    a=int(input())
    l.append(a)
for i in range(len(l)):
    for k in range(l[i]):
        if k%2==0:
            height=2*height
        else:
            height+=1
    print(f"height of {i+1} tree:",height)
    height=1