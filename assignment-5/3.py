T=int(input("Enter no. of testcases:"))
for _ in range(T):
    w=input("Enter a word:")
    w_list=list(w)
    n=len(w_list)
    i=n-2
    while i>=0 and w_list[i]>=w_list[i+1]:
        i-=1
    if i==-1:
        print("no answer")
    else:
        j=n-1
        while w_list[j]<=w_list[i]:
            j-=1
        w_list[i],w_list[j]=w_list[j],w_list[i]
        w_list[i+1:]=reversed(w_list[i+1:])
        print("".join(w_list))