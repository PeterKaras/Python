import math
from fractions import Fraction
pocet_cyklov = int(input("Zadajte pocet cyklov: "))
docasne = []
cisla = []
cisla1 = []
robots = []
celkovo = []
uhol = 0.0
pocet = 0
maxi = 0 
uhly = []
cislo1 = ""
j = 0
temp = 0
k = 0
vylucenie = 0
vylucenie2 = 0
vysledok = 0
odcitanie = 0
uhol1 = 0

while pocet_cyklov != 0:
    robot = input("Zadajte suradnice robota: ")+ " "
    
    for cislo in str(robot):
        if cislo == " ":
            robots.append(cislo1)
            cislo1 = ""
            pass
        else:
            cislo1 += cislo
    print(robots)
    
    pocet_cisiel = int(input("Zadajte pocet cisiel kt budete zadavat: "))
    
    for i in range(pocet_cisiel):
        cislo1 = ""
        suradnice = input("Zadajte suradnice ludi: ")+ " "
        for cislo in str(suradnice):
            if cislo == " ":
                docasne.append(cislo1)
                cislo1 = ""
                pass
            else:
                cislo1 += cislo
                
        vylucenie1 = (int(robots[0]) - int(docasne[0]))**2
        print(vylucenie1)

        vylucenie2 = (int(robots[1]) - int(docasne[1]))**2
        print(vylucenie2)
        
        vysledok = (vylucenie1 + vylucenie2)**(1/2)
        print(vysledok)
        
        k += 1
        print(vysledok,float(robots[2]))
        if float(vysledok) <= float(robots[2]):
            cisla.append(docasne[0])
            cisla.append(docasne[1])

        k = 0
        j = 0
        cislo1 = ""
        docasne = []
        vysledok = 0
    
    print(cisla)
    cisla1 = cisla
    dlzka = len(cisla)//2
    j = 0
    k = 1
    for cislo in range(dlzka):
        prve_cislo = int(cisla[j])- int(robots[0]) 
        druhe_cislo = int(cisla[k]) - int(robots[1])
            
        #print(prve_cislo)
        #print(druhe_cislo)
        
        if prve_cislo == 0 or druhe_cislo == 0:
            if int(cisla[j]) > int(robots[0]) and int(cisla[k]) == int(robots[1]):
                uhly.append(0)
            elif int(cisla[j]) == int(robots[0]) and int(cisla[k]) > int(robots[1]):
                uhly.append(90)
            elif int(cisla[j]) < int(robots[0]) and int(cisla[k]) == int(robots[1]):
                uhly.append(180)
            elif int(cisla[j]) == int(robots[0]) and int(cisla[k]) < int(robots[1]):
                uhly.append(270)
            elif int(cisla[j]) == int(robots[0]) and int(cisla[k]) == int(robots[1]):
                uhly.append(0)
        else:
            uhol = (math.atan(druhe_cislo / prve_cislo)) * 180 / math.pi
            #print(uhol)
            if int(cisla[j]) > int(robots[0]) and int(cisla[k]) > int(robots[1]):
                uhly.append(uhol)
            elif int(cisla[j]) < int(robots[0]) and int(cisla[k]) > int(robots[1]):
                uhol *= -1
                uhol1 = uhol + 90
                uhly.append(uhol1)
            elif int(cisla[j]) < int(robots[0]) and int(cisla[k]) < int(robots[1]):
                uhol1 = uhol + 180
                uhly.append(uhol1)
            elif int(cisla[j]) > int(robots[0]) and int(cisla[k]) < int(robots[1]):
                uhol *= -1
                uhol1 = uhol + 270
                uhly.append(uhol1)
    
        #print(uhly)     
        prve_cislo = 0
        druhe_cislo = 0
        uhol = 0
        uhol1 = 0
        j += 2
        k += 2
    #print(uhly)  
    k = 0
    j = 0
    for j in range(len(uhly)-1,0,-1):
        for k in range(j):
            if uhly[k] > uhly[k+1]:
                temp = uhly[k]
                uhly[k] = uhly[k+1]
                uhly[k+1] = temp    
    uhol = 0    
    j = 0
    k = 0
    #print(uhly)    
    for cislo in uhly:
        uhol= uhly[j] + 180
        #print(uhol)
        for cislo3 in uhly:
            if k <= j:
                k += 1
                pass
            else:
                if uhly[j] <= uhly[k] <= uhol:
                    if uhly[k] > uhly[j]:
                        pocet += 1
                        #print(uhly[k])
                k += 1
                
        uhol = 0
        j += 1
        k = 0
        if maxi < pocet:
            maxi = pocet
        pocet = 0
        
    j = 0
    k = 0
             
    print(maxi+1)            
    docasne = []
    cisla = []
    cisla1 = []
    robots = []
    celkovo = []
    uhol = 0
    pocet = 0
    maxi = 0 
    uhly = []
    cislo1 = ""
    j = 0
    temp = 0
    k = 0
    vylucenie = 0
    vylucenie2 = 0
    vysledok = 0
    celkovo = 0
    uhol1 = 0
    pocet_cyklov -= 1
