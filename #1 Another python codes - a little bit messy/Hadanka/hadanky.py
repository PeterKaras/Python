def otvaranie():
    subor = open("hadanka.txt","r")
    slovo = subor.read()
    subor.close()
    return slovo

def kontrola(slovo,medzera=""):
    for pismeno in slovo:
        if pismeno == " ":
            pass
        else:
            medzera += pismeno
    return medzera

def hlavny_cyklus(znaky,slovo,uhadnutie="",slovo1=[],i=0):
    while True:
        hadanie = input("Zadajte vase pismeno: ").strip()
        if hadanie in uhadnutie:
            print("Už ste toto písmeno uhádli!\n")
        elif hadanie in slovo:
            uhadnutie += str(hadanie)
            print("Uhádli ste!\n")
            slovo1 = indexovanie(slovo,znaky,hadanie)
            if slovo1[0] == slovo:
                break
        else:
            print("Skúste znovu!\n")

def indexovanie(slovo,znaky,hadanie,nove_slovo="",i=0,kon=""):
    for pismeno in slovo:
        if pismeno == hadanie:
            znaky[i] = hadanie
        else:
            pass
        i += 1
    for pismeno in znaky:
        nove_slovo += (pismeno) + " "
        kon += pismeno 
    print(nove_slovo)
    return kon,znaky

slovo = otvaranie()
slovo1 = kontrola(slovo)
print(len(slovo1)*"_ ")
hlavny_cyklus(list(len(slovo1)*"_"),slovo1)
