pocet_hier = int(input("Zadajte pocet hier: "))
cisla = []
porovnanie = ""
cislo = 0
najviac = 0
cislo1 = 0

while pocet_hier != 0:
    vyriesene_priklady = int(input("Zadajte pocet kol v jednej hre: "))
    
    for i in range(vyriesene_priklady):
        cislo_sutaziaceho = int(input("Zadajte cislo sutaziaceho :"))
        cisla.append(cislo_sutaziaceho)
        cislo = cisla.count(cislo_sutaziaceho)
        if cislo > cislo1:
            najviac = cislo_sutaziaceho
            cislo1 = cislo
    
            
        
    print("Vyhrava hrac s cislom",najviac)
    cislo1 = 0
    naviac = 0
    cisla = []
    pocet_hier -= 1  
