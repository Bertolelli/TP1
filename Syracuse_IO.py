print("Entrez un entier strictement positif : ", end="")
var = int(input())
L = [float(var)]
f = open("Ret.txt", "w")
var2 = float(var)
f.write(str(var2))
f.write(", ")
while var !=1:
    if var%2==0:
        var = var/2
        L.append(var)
        f.write(str(var))
        if var != 1:
            f.write(", ")
    elif var%2!=0:
        var = var*3+1
        L.append(var)
        f.write(str(var))
        if var != 1:
            f.write(", ")
f.close()
F = open("Ret.txt", "r")
print(L)
print(F.read())
F.close()