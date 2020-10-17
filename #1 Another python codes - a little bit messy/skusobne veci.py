i = 164479
#print(list(i)) doesnt work if variable is int
print(len(str(i)))
text = "halo_S"
if "_" in text:
    print("ok")

cisla = [[1,2,3,4,5],[1,2,6,4,5],[1,2,4,4,5]]
print(cisla[::-1])

cisla = {}

#cisla.update({"2":list("2")})
cisla.setdefault("2",[]).append("4895")
cisla.setdefault("2",[]).append("488")
for i in range(len(cisla["2"])-1,0,-1):
    for j in range(i):
        if int(cisla["2"][j]) > int(cisla["2"][j+1]):
            temp = cisla["2"][j]
            cisla["2"][j] = cisla["2"][j+1]
            cisla["2"][j+1] = temp
for cislo in cisla["2"]:
    print(cislo)
print(cisla)
if "2" in cisla:
    print(cisla["2"])
else:
    print("dpce")
nove = ""
cisla = [1,2,3]
nove = " ".join(str(znak) for znak in cisla)
print(nove)
cisla = {'2': ['5', '1'], '3': ['4']}
print(len(cisla))
for pismeno in cisla:
    print(pismeno)
cisla = [1,2,3,4,5],[1,2,6,4,5],[1,2,4,4,5]
from itertools import product
i = 0
for meno in product(*cisla):
    print(meno)
    
string = ['FIaIT', 'fakulta', 'informatiky', 'a', 'informacnych', 'technologii']
print(string[0][1])
print(string[1].count("f"))

print(15%1)

pole = "pole"
pole = pole.replace(pole[0], "")
print(pole)
pole += "P"
print(pole)
for k in range(4):
    pole = pole.replace(pole[0], "")
    pole += "P"
    print(pole)

word = ""
hladane = "L"
indexy = []
guess = ["LUK"]
pole = [['A', 'H', 'O', 'J'], ['B', 'U', 'M', 'O'], ['K', 'L', 'U', 'K']]
#for i in range(3):
   # print(pole[i].index("O"))
"""for k in range(3):
    hladane = pole[k][0]
    for i in range(len(pole)):
        for j in range(len(pole[i])):
            if pole[i][j] == hladane:
                p = list(str(i)+str(j))
                indexy.append(p)
    print(indexy)
    indexy = []
    
zaciatok = indexy[2][1]
print(zaciatok)
for i in range(len(pole[zaciatok])):
    if (int(self.indexy[k][p+1]) - pocet)+1 <= j:
        word += self.field[zaciatok][j]
    if j == int(self.indexy[k][p+1]):
        word += "L"
        if word[::-1] in guess:
             print("ok")
        else:
            print(word)"""
slovo = "po4l"
if slovo.isalpha():
    print("HALO")
else:
    print("NE")
for i in range(2):
    print(i)
    
find_index = "".join(slovo).find("po")
print(find_index)

x = lambda a: a + 10
print(x(5))
listy = "peto"
listy1 = "pato"

for pismeno in listy,listy1:
    print(pismeno)

pole = [['00:14', 'Londyn', 'Pariz']]

for badge in pole[0]:
    #print(badge)
    print(int(badge[3:5])+30//60)
    
    break
