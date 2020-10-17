slovnik = {"1":["2","3","4","5"],
           "2":["5","4","6","6"],
           "3":["4","5"],
           "4":["7","8"],
           "11":["14"],
           "15":["14"]}
for i in slovnik:
    print(i)

try:
    for x in slovnik["15"]:
        print(x)
        print(slovnik[x])
        if "15" in slovnik[x]:
            print("riesim")
except KeyError:
    print("vydudli mi koket!")
        
"""res = list(slovnik.keys())[0] 
print(res)
#print(slovnik[str(res)])
#res = str(res)
for x in slovnik[str(res)]:
    print(x)
    if res == list(x):
        print("chod do pice")
    else:
        print("nic")"""

pole = "06"
if int(pole)>0:
    print(pole)

for x in slovnik:
    print("x",x)
if "11" in slovnik["3"]:
    print("nic")
else:
    print("OK")

#print(slovnik.find("2"))

pole = []
for i in range(2):
    pole.append(["-1" for i in range(4)])
print(pole)

print(23%6)
print(5%6)

steps = 4
bound = 0

for _ in range(4):
    print("h",steps-(steps-bound))
    bound += 1

pole= ["1","1"]
print(tuple(pole))

path = [(1, 4), (1, 5), (1, 6)]
path.pop(0)
path.pop(len(path)-1)
print(path)

#print((str(21)+str(22).split()))

pole = ["1","2","3","4","5"]
new = []
new.append(pole[0:2])
print(pole[0:2])
