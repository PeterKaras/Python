num_env = 9
slovo = "middle"
field = []
if (num_env//2)-1 >= 4:
    num_homes = 4
else:
    num_homes = (num_env//2)-1
print(num_homes)
separator = (num_env//2)+1
print(separator)
string = ""
indexy = []
num_paths = (num_env-1)*4
print(num_paths)

for i in range(separator):
    #print(i)
    if slovo == "middle":
        string = "*" + num_homes*"O" + (num_env-((num_homes+1)*2))*" " + num_homes*"O" + "*"
        field.append(list(string))
        slovo = "semiMiddle"
    elif slovo == "semiMiddle":
        string = (separator)*"*" + "O" + (separator)*"*"
        field.insert(0,list(string))
        field.append(list(string))
        slovo = "notMiddle"
    else:
        if i == separator-1:
            field.insert(0,list("***"))
            field.append(list("***"))
        else:
            #print(i)
            if i >= separator-num_homes:
                field.insert(0,list("*O*"))
                field.append(list("*O*"))
            else:
                field.insert(0,list("* *"))
                field.append(list("* *"))
    
print(field)
