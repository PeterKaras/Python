i = 0
j = 0
k= 0
listy = ["A","A","B","A","C","C","C","C","A","B","A","A"]
prazdna = ""
docasne = []
prazdne = []
pocet = 1
docasne1 = ""
dlzka = 0
heslo = "AABACCCCABAA"
porovnanie = ""


for pismeno in listy:#HLAVNY CYKLUS
    listy[i] = " "
    #print(listy)
    for pismeno in listy: #VEDLAJSI CYKLUS
        if pismeno == " ":
            continue
        else:
            prazdna += pismeno
    #prazdne.append(prazdna) 
    if docasne == []:
        docasne.append(prazdna)
        print(docasne) 
    else:
        for slovo in docasne:
            docasne1 = docasne[j]
            #print(docasne[j])
            if prazdna == docasne1:
                pass
            else:
                j += 1
                docasne.append(prazdna)
                break
            
    print(docasne)    
    listy = []
    for pismeno in heslo:
        listy.append(pismeno)   
    prazdna = ""
    porovnanie = listy[i]
    i += 1
    #j = 0
    prazdne = []
