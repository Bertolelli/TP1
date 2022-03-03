var1 = int(input())
sample = var1
var2 = int(input())
i=1
LV1 = [var1]
LV2 = [i]

while i < var2 :
    var1 = var1+var1
    LV1.append(var1)
    i=i+i
    LV2.append(i)
    if i == var2:
        print(LV1)
        print(LV2)
        print("Le résultat de ", sample," x ", var2, " est : ", var1)
    else:
        t = len(LV2)
        LV1.pop(t)
        LV2.pop(t)
        test = var2 - LV2[t]
        '''if test in LV2 :
            var1 = var1 + '''