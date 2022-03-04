print("Entrer un entier strictement positif : ", end="")
var = int(input())
L = [var]
while var !=1:
    if var%2==0:
        var = var//2
        L.append(int(var))
    elif var%2!=0:
        var = var*3+1
        L.append(var)
print(L)