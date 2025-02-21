T=int(input("Enter no.of testcases:"))
l=input().split( )
for i in l:
    count=0
    j=int(i)
    for k in range(1,j+1):
        a=k//2
        count+=a
    print(count)
