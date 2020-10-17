znaky = []
medzera = 0



subor = open("Znaky.txt","r")

slovo = subor.read()
print(slovo)
subor.close()

for znak in slovo:
    znaky.append(znak)

for znaky in znaky:
    znak = znaky.lower()
    if znak == "x" or znak == "y":
        print("precital som",znak)
        continue
    elif znak == "#" or znak == "$" or znak == "&":
        print("precital som riadiaci znak")
        continue
    elif znak == " ":
        medzera += 1
        continue
    elif znak == "*":
        print("koniec\n")
        break
    else:
        continue

print("pocet precitanych medzier:",medzera)
