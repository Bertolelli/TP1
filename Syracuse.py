print("Entrer un entier strictement positif : ")
var = int(input())
L = [float(var)]
while var !=1:
    if var%2==0:
        var = var/2
        L.append(var)
    elif var%2!=0:
        var = var*3+1
        L.append(var)
print(L)