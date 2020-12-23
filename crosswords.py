class Loadings:
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width
        
    def loading(self):
        crosswords = []
        words = []
        for i in range(2):
            while True:
                amount = self.stating_amount(i)
                if str(amount).isdigit():
                    break            
            while amount:
                row = input("Input your row of crossword: ").strip()
                if (len(row) == self.width or i == 1)and self.checking(row) != "Revise":
                    if i == 0:
                        crosswords.append(list(row))
                    else:
                        words.append(list(row))
                else:
                    print("Wrong Input!")
                    continue
                amount -= 1
        return crosswords,words

    def stating_amount(self,i):
        if i == 0:
            return self.lenght
        else:
            amount = input("Input your amount of finding words: ").strip()
            if amount.isdigit():
                return int(amount)
            else:
                print("Wrong Input!")

    def checking(self,row):
        for letter in row:
            if 65 <= ord(letter.upper()) <= 90:
                pass
            else:
                return "Revise"

class Portraying:        
    def main_loop_port(self):
        for part in self.main_indexes:
            for i in range(0,len(part),2):
                self.crosswords[int(part[i])][int(part[i+1])] = "0"
                if i+1 >= len(part)-2:
                    break
        return self.depicting()
    def depicting(self):
        result = ""
        for line in self.crosswords:
            print("".join(line))
            for i in range(len(line)):
                if line[i] != "0":
                    result += line[i]
        return result
        
class Main(Loadings,Portraying):
    def __init__(self,lenght,width):
        Loadings.__init__(self,lenght,width)
        self.crosswords,self.words = super().loading()
        self.main_indexes = []
        
    def main_loop(self):
        for word in self.words:
            indexes = self.indexing(word[0])
            self.vertical(word,indexes)

    def indexing(self,letter):
        indexes = []
        for i in range(len(self.crosswords)):
            if letter in self.crosswords[i]:
                for j in range(len(self.crosswords[i])):
                    if self.crosswords[i][j] == letter:
                        indexes.append((str(i)+ " " + str(j)).split(" "))
        return indexes

    def vertical(self,word,indexes):
        down_merger,up_merger = word[0],word[0]
        for stance in indexes:
            index_down,index_up = str(stance[0]) + " " + str(stance[1]) + " ",str(stance[0]) + " " + str(stance[1]) + " "
            for i in range(len(self.crosswords)):
                if int(stance[0])-i > -1 and down_merger == "".join(word[:i+1]):
                    down_merger += self.crosswords[int(stance[0])-(i+1)][int(stance[1])]
                    index_down += str(int(stance[0])-(i+1)) + " " + str(int(stance[1])) + " "
                if int(stance[0])+i < len(self.crosswords)-1 and up_merger == "".join(word[:i+1]):
                    up_merger += self.crosswords[int(stance[0])+(i+1)][int(stance[1])]
                    index_up += str(int(stance[0])+(i+1)) + " " + str(int(stance[1])) + " "
                    
                if up_merger.upper() == ("".join(word)).upper():
                    self.main_indexes.append(index_up.split(" "))
                    return 0
                elif down_merger.upper() == ("".join(word)).upper():
                    self.main_indexes.append(index_down.split(" "))
                    return 0

                if down_merger != "".join(word[:i+2]) and up_merger != "".join(word[:i+2]):
                    if self.horizontal(word,stance) == "Ok":
                        return 0
                
            down_merger,up_merger = word[0],word[0]

    def horizontal(self,word,stance):
        index_down,index_up = str(stance[0]) + " " + str(stance[1]) + " ",str(stance[0]) + " " + str(stance[1]) + " "
        down_merger,up_merger = word[0],word[0]
        for i in range(len(self.crosswords)):
            if int(stance[1])-(i+1) > -1 and down_merger == "".join(word[:i+1]):
                down_merger += self.crosswords[int(stance[0])][int(stance[1])-(i+1)]
                index_down += str(int(stance[0])) + " " + str(int(stance[1])-(i+1)) + " "
            if int(stance[1])+(i+1) < len(self.crosswords[0])+1 and up_merger == "".join(word[:i+1]):
                up_merger += self.crosswords[int(stance[0])][int(stance[1])+(i+1)]
                index_up += str(int(stance[0])) + " " + str(int(stance[1])+(i+1)) + " "      
            if down_merger != "".join(word[:i+2]) and up_merger != "".join(word[:i+2]):
                if self.diagonal(word,stance) == "Ok":
                    return "Ok"
                
            if up_merger.upper() ==  ("".join(word)).upper():
                self.main_indexes.append(index_up.split(" "))
                return "Ok"
            elif down_merger.upper() == ("".join(word)).upper():
                self.main_indexes.append(index_down.split(" "))
                return "Ok"

    def diagonal(self,word,stance):
        dr_merger,ur_merger,dl_merger,ul_merger = word[0],word[0],word[0],word[0]
        dr_index,ur_index = str(stance[0]) + " " + str(stance[1]) + " ",str(stance[0]) + " " + str(stance[1]) + " "
        dl_index,ul_index = str(stance[0]) + " " + str(stance[1]) + " ",str(stance[0]) + " " + str(stance[1]) + " "
        for i in range(len(self.crosswords)):
            if int(stance[0])-(i+1) > -1 and int(stance[1])-(i+1) > -1 and ul_merger == "".join(word[:i+1]):
                ul_merger +=  self.crosswords[int(stance[0])-(i+1)][int(stance[1])-(i+1)]
                ul_index += str(int(stance[0])-(i+1)) + " " + str(int(stance[1])-(i+1)) + " "
           
            if int(stance[0])+(i+1) < len(self.crosswords) and int(stance[1])+(i+1) < len(self.crosswords[0]) \
               and dr_merger == "".join(word[:i+1]):
                dr_merger += self.crosswords[int(stance[0])+(i+1)][int(stance[1])+(i+1)]
                dr_index += str(int(stance[0])+(i+1)) + " " + str(int(stance[1])+(i+1)) + " "
           
            if int(stance[0])-(i+1) > -1 and 0 < int(stance[1])+(i+1) < len(self.crosswords[0]) and \
               ur_merger == "".join(word[:i+1]):
                ur_merger += self.crosswords[int(stance[0])-(i+1)][int(stance[1])+(i+1)]
                ur_index += str(int(stance[0])-(i+1)) + " " + str(int(stance[1])+(i+1)) + " "
        
            if int(stance[0])+(i+1) < len(self.crosswords[0]) and int(stance[1])-(i+1) > -1 and \
               dl_merger == "".join(word[:i+1]):
                dl_merger += self.crosswords[int(stance[0])+(i+1)][int(stance[1])-(i+1)]
                dl_index += str(int(stance[0])+(i+1)) + " " + str(int(stance[1])-(i+1)) + " "

            if ul_merger.upper() == ("".join(word)).upper():
                self.main_indexes.append(ul_index.split(" "))
                return "Ok"
            elif dr_merger.upper() == ("".join(word)).upper():
                self.main_indexes.append(dr_index.split(" "))
                return "Ok"
            elif ur_merger.upper() == ("".join(word)).upper():
                self.main_indexes.append(ur_index.split(" "))
                return "Ok"
            elif dl_merger.upper() == ("".join(word)).upper():
                self.main_indexes.append(dl_index.split(" "))
                return "Ok"
                  
    def __str__(self): 
        self.main_loop()
        return self.main_loop_port()

loop = input("Loop: ").strip()
if len(loop)>= 1 and loop.isdigit():
    while int(loop):
        range_field = input("Input range of field: ").split()
        if len(range_field)==2 and range_field[0].isdigit() and range_field[1].isdigit():
            print(Main(int(range_field[0]),int(range_field[1])))
        else:
            print("Wrong input! Once again")
            continue
        loop = int(loop)-1
else:
    print("Wrong Input!")
