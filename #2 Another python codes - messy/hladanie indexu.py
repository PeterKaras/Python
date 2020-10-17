cisla = ["2", "3", "2", "1", "4", "2", "3"]
cisla1 = "2321423"
hviezdy = ['*', '*', '*', '*', '*', '*', '*']
index2 = []
index3 = 0

i = 3
j = 0

for cislo in cisla: 
    if cisla[j] == str(i):
        index2.append(str(j))
        
    j += 1
print(index2)
i -= 1
j = 0
index2 = []
