pocet = int(input("Zadajte pocet opakovani: "))
listy = []
cisla = []
string = ""
i = 0
vysledok = 0
vysledok1 = 0


while pocet != 0:
    znaky = input("Zadajte vasu vetu: ")
    for znak in znaky:
        listy.append(znak)
    listy += " "
    print(listy)
    
    for znak in listy:
        if znak.isdigit() == True:
            string += znak
            if listy[i+1].isdigit() == False:
                vysledok += int(string)
                #print(string,vysledok)
                string = ""
        else:
            cisla.append(znak)
        
        i += 1
    if cisla == listy:
        print("Nebolo najdene ziadne cislo!")
    else:
        print(vysledok)
        
    i = 0
    vysledok = 0
    vysledok1 = 0  
    string = ""
    pocet -= 1
    listy = []
    cisla = []
        
