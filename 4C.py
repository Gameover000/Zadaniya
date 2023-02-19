spiski = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
col = 9
stroka = 0
ter = 0
for i in spiski:
    if stroka % 2 == 0:
        for n in i:
            ter += 1
            i[col] = ter
            col -= 1
            if col < 0:
                col += 1
                stroka += 1
    else:
        for n in i:
            ter += 1
            i[col] = ter
            col += 1
            if col > 9:
                col -= 1
                stroka += 1
i = len(spiski ) - 1
while True:
    print(spiski[i])
    i -= 1
    if i == 0:
        print(spiski[i])
        break