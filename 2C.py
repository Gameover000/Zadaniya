def Slice(text,znak):
    spisok = []
    a = ""
    for i in text:
        if i != znak:
            a += i
        else:
            spisok.append(a)
            a = ""
    return spisok
a = str(input())
b = str(input())
aSlise = Slice(a,".")
bSlise = Slice(b,".")
maxlen = len(aSlise)
if len(bSlise) > maxlen:
    maxlen = len(bSlise)
for i in range(0,maxlen):
    if aSlise[i] == bSlise[i]:
        pass
    elif aSlise[i] > bSlise[i]:
        print(a)
        break
    elif aSlise[i] < bSlise[i]:
        print(b)
        break