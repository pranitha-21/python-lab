T=int(input("Enter no. of test cases:"))
a=[]
for i in range(T):
    s=input()
    a.append(s)
for i in range(T):
    b=a[i]
    n=len(b)
    count = 0
    for i in range(n // 2):
        count += abs(ord(b[i]) - ord(b[n - i - 1]))
    print(count)