import math
T=int(input("Enter no. of test cases:"))
l=[]
for i in range(T):
    a,b=input().split( )
    l.append(int(a))
    l.append(int(b))

for i in range(0,len(l),2):
    s=[]
    for k in range(int(math.sqrt(l[i])),int(math.sqrt(l[i+1]))+1):
        s.append(k*k)
    count=0
    for j in range(len(s)):
        if s[j]>=l[i] and s[j]<=l[i+1]:
            count+=1
    print(count)