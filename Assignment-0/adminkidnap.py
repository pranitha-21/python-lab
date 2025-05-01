T=input("Enter no.of test cases")
T=int(T)
i=0
while i<T:
    N=input("N=")
    N=int(N)
    X=input("X=")
    X=int(X)
    S=input("S=")
    S=int(S)
    while i<S:
        A=input("A=")
        A=int(A)
        B=input("B=")
        B=int(B)
        i+=1
        if B==X:
            X=A
        else:
            X=B

print(X)