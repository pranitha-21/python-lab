testcases=int(input("Enter no. of test cases:"))
c=[]

for i in range(testcases):
    c.append(int(input("Enter number:")))

for i in c:
    k=i
    count=0
    while i!=0:
        q=i%10
        if k%q==0:
            count+=1
        i=i//10
    print(count)
