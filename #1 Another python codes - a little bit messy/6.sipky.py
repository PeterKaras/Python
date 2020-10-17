def kontrola(cisla,pocet):
    for cislo in cisla:
        if cislo.isdigit() == False:
            return "STOP" 
        else:
            pocet -= 1
            continue
    if pocet == 0:
        return "ok"
    else:
        return "STOP"
        
def nacitanie(rozmedzie,znaky = [],cyklus = 0):
    znaky = []
    for i in range(int(rozmedzie[0])):
        riadok = input("Zadajte znaky: ").strip()
        znak = kontrola1(riadok,rozmedzie)
        if znak == "ok":
            znaky.append(riadok)
        else:
            return "STOP"
    return znaky

def kontrola1(riadok,rozmedzie,pocet = 0):
    pocet = int(rozmedzie[1])
    for pismeno in riadok:
        if pismeno == "^" or pismeno == "v" or pismeno == "<" or  pismeno == ">" or pismeno == ".":
            pocet -= 1
            pass
        else:
            return "Ne"
    if pocet == 0:
        return "ok"
    else:
        return "STOP"

def hlavny_cyklus(pole,rozmedzie,pocet = 0,i = 0, j = 0,dalej= 0):
    for k in range(int(rozmedzie[1])):
        for m in range(int(rozmedzie[0])):
            if pole[m][k] == ".":
                continue
            elif pole[m][k] == "v":
                znak = downcheck(pole,rozmedzie,m,k)
            elif pole[m][k] == ">":
                znak = right_sidecheck(pole,rozmedzie,m,k)
            elif pole[m][k] == "^":
                znak = uper_check(pole,rozmedzie,m,k)
            else:
                znak = left_check(pole,rozmedzie,m,k)
    
            if znak.isdigit() == True:
                pocet += int(znak)
            else:
                if znak == "A":
                    znak = uper_check(pole,rozmedzie,m,k)
                    if znak == "N":
                        return "-1"
                    else:
                        pocet += 1
                else:
                    znak = right_sidecheck(pole,rozmedzie,m,k)
                    if znak == "A":
                        return "-1"
                    else:
                        pocet += 1
    return pocet

def right_sidecheck(pole,rozmedzie,i,j,pocet1 = 0,pocet = 1):
    if j == int(rozmedzie[1])-1:
        pass
    else:
        for m in range(int(rozmedzie[1])):
            if pole[i][j+1] != ".":
                return str(0)
            j += 1
            if j == int(rozmedzie[1])-1:  
                break
    j = 0
    for m in range(int(rozmedzie[1])):
        if pole[i][j] != ".":
            pocet1 += 1
            if pocet1 == 2:
                return str(pocet)
        j += 1
    return "A"

def left_check(pole,rozmedzie,i,j,pocet1 = 0,pocet = 1):
    if j == 0:
        pass
    else:
        for m in range(int(rozmedzie[1])):
            if pole[i][j-1] != ".":
                return str(0)
            j -= 1
            if j == 0:
                break
    j = 0
    for m in range(int(rozmedzie[1])):
        if pole[i][j] != ".":
            pocet1 += 1
            if pocet1 == 2:
                return str(pocet)
        j += 1   
    return "A"

def downcheck(pole,rozmedzie,i,j,pocet1=0,pocet = 1):
    if i == int(rozmedzie[0])-1:
        pass
    else:
        for m in range(int(rozmedzie[0])):
            if pole[i+1][j] != ".":
                return str(0)
            i += 1
            if i == int(rozmedzie[0])-1:
                break
    i = 0
    for m in range(int(rozmedzie[0])):
        if pole[i][j] != ".":
            pocet1 += 1
            if pocet1 == 2:
                return str(pocet)
        i += 1
    return "N"

def uper_check(pole,rozmedzie,i,j,pocet1=0,pocet = 1):
    if i == 0:
        pass
    else:
        for m in range(int(rozmedzie[0])):
            if pole[i][j] != ".":
                return str(0)
            i -= 1
            if i == -1:
                break
    i = 0
    for m in range(int(rozmedzie[0])):
        if pole[i][j] != ".":
            pocet1 += 1
            if pocet1 == 2:
                return str(pocet)
        i += 1
    return "N"

cyklus = input("Pocet cyklov: ").strip()
if cyklus.isdigit() == True:
    while int(cyklus) != 0:
        rozmedzie = input("Zadajte rozmedzie pola: ").split()
        if kontrola(rozmedzie,pocet = 2) == "ok":
            pole = nacitanie(rozmedzie)
            if pole == "STOP":
                continue
            else:
                print(hlavny_cyklus(pole,rozmedzie))
        else:
            print("Nezadali ste pozadovany pristup!")
            continue
    
        cyklus = int(cyklus) - 1
else:
    print("Nezadali ste cislo!")
