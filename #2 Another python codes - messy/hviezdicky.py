i = int(input("Zadajte pocet hviezdiciek kt chcete mat: "))
j = 0
hviezdicky = ""
pocet = i

while i != 0:
    if i == 0:
        print("Nezadali ste ziadny pocet")
    else:
        hviezdicky = "*" * i
        print(hviezdicky)


    i -= 1
    hviezdicky = ""

while j != (pocet+1):
    if j == 0 or j == 1:
        pass
    else:
        hviezdicky = "*" * j
        print(hviezdicky)


    j += 1
    hviezdicky = ""
