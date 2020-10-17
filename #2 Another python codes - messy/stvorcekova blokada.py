pocet_cyklov = int(input("Zadajte pocet cyklov: "))
riadiace = []
x = []
y = []
pocet = 0
sur_x = 0
sur_y = 0
spojitko = ""
i = 0
j = 0
koniec = ""
docasne_x = []
docasne_y = []
zvysok = 0
pomocna = ""
zvysok1 = 0
pocet1 = 0
pocet2 = 0
neda = ""
hore = 0
dole = 0


while pocet_cyklov != 0:
    riadiacie1 = input("Zadajte pocet prekazok a pocet krokov: ") + " "
    for cislo in str(riadiacie1):
        
        if cislo == "-":
            spojitko += "-"
        elif cislo.isdigit() == True:
            spojitko += str(cislo)
        elif cislo == " ":
            if spojitko == "":
                pass
            else:
                riadiace.append(spojitko)
                spojitko = ""
    #print(riadiace)

    spojitko = ""
    for cislo1 in range(int(riadiace[0])):
        suradnice1 = input("Zadajte suradnice prekazok: ")
        for cislo in str(suradnice1):
            if cislo == " ":
                pass
            elif cislo == "-":
                spojitko += cislo
            elif pocet == 0:
                if spojitko != "":
                    spojitko += cislo
                    x.append(spojitko)
                else:
                    x.append(cislo)
                spojitko = ""
                pocet += 1
            else:
                if spojitko != "":
                    spojitko += cislo
                    y.append(spojitko)
                else:
                    y.append(cislo)
                spojitko = ""
                pocet = 0
    #print(x)
    #print(y)
    pocet = 0
    spojitko = ""
    for cislo in range(int(riadiace[1])):
        if neda == "neda":
            break
        for cislo1 in x:
            zvysok = int(x[i]) - sur_x
            if zvysok < 0:
                zvysok *= -1

            if zvysok == 1 or zvysok == 0:
                docasne_x.append(x[i])
                docasne_y.append(y[i])
    
            i += 1

        i = 0
        #print("x",docasne_x)
        #print("y",docasne_y)
        if docasne_x == []:
            sur_x += 1
            pocet += 1
            koniec == "koniec"
            #print("HUH")
        else:
            for cislo2 in docasne_x:
                #print("Kokot")
                if int(cislo2)-1 == sur_x:
                    #print("A sem tu zas")
                    if int(docasne_y[i]) != sur_y:
                        #print("prvy",docasne_y[i],sur_y)
                        #pocet += 1
                        #sur_x += 1
                        pomocna = ""
                    else:
                        #print("druha")
                        #sur_y += 1
                        pomocna = "aha"

                    if pomocna == "aha":
                        break
                i += 1
                
            #print("eqweqw!")
                
            for cislo3 in docasne_y:
                #print("skaasdp")
                #zvysok1 = int(docasne_y[j]) - sur_y
                if pomocna == "":
                    break
                
                if (sur_y+1) == int(docasne_y[j]) and sur_x == int(docasne_x[j]):
                    #print("skap")
                    pocet1 += 1
                elif (sur_y-1) == int(docasne_y[j]) and sur_x == int(docasne_x[j]):
                    #print("YEiYE")
                    pocet1 += 1
                
                if pocet1 == 2:
                    neda = "neda"
                    #sur_y = 0
                    break
                
                j += 1
                
            i = 0
            j = 0

            if pomocna == "aha":
                for cislo4 in docasne_y:
                    if int(cislo4) > 0:
                        #print(cislo4)
                        hore += 1
                    elif int(cislo4) < 0:
                        dole += 1
                    else:
                        pass
            
            if koniec == "koniec":
                pass
            else:
                if pomocna == "":
                    pocet += 1
                    sur_x += 1
                else:
                    if hore > dole:
                        sur_y -= 1
                    elif hore < dole:
                        sur_y += 1
                    else:
                        sur_y += 1
                        
        docasne_y = []
        docasne_x = []
        i = 0
        j = 0
        pocet1 = 0
        koniec == ""
        pomocna = ""
        print(sur_x,sur_y)

    if int(riadiace[0]) == 0:
        print(int(riadiace[1]))
    else:
        print(pocet)

    riadiace = []
    x = []
    y = []
    pocet = 0
    sur_x = 0
    sur_y = 0
    spojitko = ""
    i = 0
    j = 0
    koniec = ""
    docasne_x = []
    docasne_y = []
    zvysok = 0
    pomocna = ""
    zvysok1 = 0
    pocet1 = 0
    pocet2 = 0
    neda = ""
    pocet_cyklov -= 1
