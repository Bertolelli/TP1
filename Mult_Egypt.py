def ME(a,b):
    A = a
    B = b
    S = 0
    while A != 0:
        if A%2 == 1:
            S = S+B
        A = A//2
        B = B+B
    return S

print("Saisir un premier entier : ", end="") 
a = int(input())
print("Saisir le Second entier : ", end="")
b = int(input())

ret = ME(a,b)
print("le résultat de : ", a, "*", b, "est : ", ret)