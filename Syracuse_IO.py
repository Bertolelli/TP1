class Cfile(object):
    def __init__(self, fn):
        self.fn = fn
    def wri(self, msg):
        with open(self.fn, 'a') as myFile :
            myFile.write(msg)
    def rea(self):
        with open(self.fn, 'r') as readFile :
            rf = readFile.read()
            print(rf)
    def clo(self):
        with open(self.fn) as closeFile :
            closeFile.close()
    def rl(self):
        with open(self.fn, 'r') as readLine :
            rel = readLine.readlines()
            if rel is not None:
                return 1
            # print(rel)
    def dele(self, msg):
        with open(self.fn, 'w') as deleteContent:
            deleteContent.write(msg)

cf = Cfile('Ret.txt')
re = cf.rl()
if re == 1:
    cf.dele("")

print("Entrez un entier strictement positif : ", end="")
var = int(input())
L = [float(var)]
var2 = float(var)
cf.wri(str(var2))
cf.wri(", ")
while var != 1:
    if var%2==0:
        var = var/2
        L.append(var)
        cf.wri(str(var))
        if var != 1:
            cf.wri(", ")
    elif var%2 != 0:
        var =  var*3+1
        L.append(var)
        cf.wri(str(var))
        if var != 1:
            cf.wri(", ")

print("\n", L, "\n")
cf.rea()
cf.clo()