import random

#This code was designed to practice your basic knowledge in math
#There are many operations for instance multiplying, plus, minus, division, root , square and many more
#First of all, you have to choose your difficulty of your practice
#If you decide to move on another level u have press letter P
#To show result of exercise you have to press V
#To end whole program u have to press K

class EasyLevel:
    def __init__(self):
        self.compliments = ["Good","Excelent","Nice One","Keep going","Awesome","Nice","Good Job","Too good","Interesting!"]
        self.resentments = ["Maybe Next time","Bad","Wrong","Not good","Enhance your Knowledge","Nah!","Learn!","Dumb","As usual, Wrong!"]
        self.punctions = {"plus":"+","minus":"-","divide":"/","multiply":"*"}
    
    def exercice(self,my_list,com):
        if int(my_list[1]) < 0:  
            print(my_list[0],com,"("+str(my_list[1])+")","= ?")
        else:
            print(my_list[0],com,my_list[1],"= ?")
            
    def result(self,my_list,result,com):
        if int(my_list[1]) < 0:  
            print(my_list[0],com,"("+str(my_list[1])+")","=",result)
        else:
            print(my_list[0],com,my_list[1],"=",result)
            
    def end(self,result,guess):
        if int(guess) == int(result):
            com = random.choice(self.compliments)
        else:
            com = random.choice(self.resentments)
            print("This is result of exercise:",result)
        print(com,"\n")
    
    def generation(self,i,b):
        return random.randint(i,b)
    
    def num_check(self,g):
        if g.strip("-").isdigit():
            return "Ok"
        return "Revise"
    
    def multiplying(self,bounds,b1):
        first = self.generation(bounds[0], bounds[1])
        second = self.generation(b1[0], b1[1])
        result = first * second 
        self.exercice([first,second],"*")
        helper = "multiply"
        return first,second,result,helper
    
    def plusing(self,b1):
        first = self.generation(b1[0], b1[1])
        second = self.generation(b1[0], b1[1])
        result = first + second 
        self.exercice([first,second],"+")
        helper = "plus"
        return first,second,result,helper
    
    def minising(self,b1):
        first = self.generation(b1[0], b1[1])
        second = self.generation(b1[0], b1[1])
        result = first - second
        self.exercice([first,second],"-")
        helper = "minus"
        return first,second,result,helper
    
    def easy_loop(self, word="ok",helper=""):
        while True:
            command = random.choice("1234")
            if word == "ok":
                print("\nZobrazi sa ti vysledok -- (V) \nSkoncis cely program! -- (K) \nPrepnutie Urovne o vyssie -- (P)\n")
            word ="ok"
            if command == "1":
                first,second,result,helper = self.plusing([-20, 25])
            elif command == "2":
                first,second,result,helper = self.minising([-20, 25])
            elif command == "3":
                first,second,result,helper = self.multiplying([-10, 10],[-10, 10])
            else:
                first = self.generation(-10, 10)
                second = self.generation(-10, 10)
                if second == 0 or first % second != 0:
                    word = "Ne"
                    continue
                result = first // second
                self.exercice([first,second],"/")
                helper = "divide"
            
            guess = input("Vysledok: ").strip()
            if guess.upper() == "V":
                self.result([first,second],result,self.punctions[helper])
                continue
            elif guess.upper() == "K":
                return 
            elif guess.upper() == "P":
                print()
                self.medium_loop()
                return 
            else:            
                if len(guess) >= 1 and self.num_check(guess) != "Revise":
                    self.end(result,guess)
                    continue
                print("Zadal si nespravny znak!")
              
class MediumLevel():
    def square(self,num):
        print(str(num)+"^2 = ?")
    
    def result_square(self,num,result):
        print(str(num)+"^2 =",result)
        
    def root(self,num):
        print(str(num)+"^0.5 = ? (odmocnina)")
        
    def result_root(self,num,result):
        print(str(num)+"^0.5 = (odmocnina)",result)
    
    def medium_loop(self,per = "ok",word="ok", helper = ""):
        while True:
            command = random.choice("123456")
            if word == "ok":
                print("\nZobrazi sa ti vysledok -- (V) \nSkoncis cely program! -- (K) \nPrepnutie Urovne o vyssie -- (P)\n")
            word ="ok"
            if command == "1":
                first,second,result,helper = self.plusing([-100, 125])
            elif command == "2":
                first,second,result,helper = self.minising([-100, 125])
            elif command == "3":
                first,second,result,helper = self.multiplying([-100, 125],[-5, 5])
            elif command == "4":
                first = self.generation(-10, 10)
                result = first**2
                per = "square"
                self.square(first)
            elif command == "5":
                numbers = [1,4,9,16,25,36,49,81,64,100,121,144]
                first = random.choice(numbers)
                result = first**0.5
                per = "root"
                self.root(first)
            else:
                first = self.generation(-100, 125)
                second = self.generation(-100, 125)
                if second == 0 or first % second != 0:
                    word = "Ne"
                    continue
                result = first // second
                self.exercice([first,second],"/")
                helper = "divide"
            
            guess = input("Vysledok: ").strip()
            
            if guess.upper() == "V":
                if per == "square":
                    per = "ok"
                    self.result_square(first,result)
                elif per == "root":
                    per = "ok"
                    self.result_root(first,result)
                else:
                    self.result([first,second],result,self.punctions[helper])
                continue
            elif guess.upper() == "K":
                return 
            elif guess.upper() == "P":
                self.hard_loop()
                return 
            else:            
                if len(guess) >= 1 and self.num_check(guess) != "Revise":
                    self.end(result,guess)
                    continue
                print("Zadal si nespravny znak!")

class HardLevel():
    def third_square(self,num):
        print(str(num)+"^3 (tretia mocnina) = ?")
    
    def result_sq3(self,num,result):
        print(str(num)+"^3 =",result)
    
    def hard_loop(self,word ="ok",per="ok"):
        while True:
            command = random.choice("12345673")
            if word == "ok":
                print("\nZobrazi sa ti vysledok -- (V) \nSkoncis cely program! -- (K) \nPrepnutie Urovne o vyssie -- (P)\n")
            word ="ok"
            if command == "1":
                first,second,result,helper = self.plusing([-1000, 1000])
            elif command == "2":
                first,second,result,helper = self.minising([-1000, 1000])
            elif command == "3":
                first,second,result,helper = self.multiplying([-100, 125],[-100, 100])
            elif command == "4":
                first = self.generation(-27, 27)
                result = first**2
                per = "square"
                self.square(first)
            elif command == "5":
                numbers = [12**2,13**2,14**2,12**2,15**2,16**2,17**2,18**2,19**2,20**2,21**2,22**2,24**2,25**2,26**2,27**2]
                first = random.choice(numbers)
                result = first**0.5
                per = "root"
                self.root(first)
            elif command == "6":
                first = self.generation(-15, 15)
                result = (first**2)*first
                per = "square3"
                self.third_square(first)
            else:
                first = self.generation(-1000, 1000)
                second = self.generation(-1000, 1000)
                if first % second != 0 and second != 0:
                    word = "Ne"
                    continue
                result = first // second
                self.exercice([first,second],"/")
                helper = "divide"
            
            guess = input("Vysledok: ").strip()
            
            if guess.upper() == "V":
                if per == "square":
                    per = "ok"
                    self.result_square(first,result)
                elif per == "root":
                    per = "ok"
                    self.result_root(first,result)
                elif per == "square3":
                    per = "ok"
                    self.result_sq3(first,result)
                else:
                    self.result([first,second],result,self.punctions[helper])
                continue
            elif guess.upper() == "K":
                return 
            elif guess.upper() == "P":
                self.hard_loop()
                return 
            else:            
                if len(guess) >= 1 and self.num_check(guess) != "Revise":
                    self.end(result,guess)
                    continue
                print("Zadal si nespravny znak!")
                
class Main(EasyLevel,HardLevel,MediumLevel):
    def __init__(self):
        self.command = None
        super().__init__()
        
    def checking(self,c):
        if c == "s" or c == "l" or c == "t":
            return "Ok"
        print("Nezadal si spravny znak!")

    def main_loop(self):
        print("------- Zadavaj podla pismien v zatvorke ---------")
        print("OBTIAZNOSTI: Lahka(l) | streda(s) | tazka(t) \n")
        while True:
            difficulty = input("Zadaj obtiaznost: ").strip()
            if self.checking(difficulty) == "Ok" and len(difficulty) >= 1:
                break
        
        if difficulty.lower() == "l":
            self.easy_loop()
        elif difficulty.lower() == "s":
            self.medium_loop()
        elif difficulty.lower() == "t":
            self.hard_loop()
        else:
            self.medium_loop()
        
        return "Koniec, Oddychni si a pridi spat ked budes ready!"
        
    def __str__(self):
        return self.main_loop()

if __name__ == "__main__":
    print(Main())
