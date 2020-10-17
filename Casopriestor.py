import time
class Loading:
    def __init__(self):
        self.initial = None
        self.bounds = []
        self.cities = []
        self.seperated_cities = []

    def enquiry(self):
        self.initial = input("Zadajte rozmedzie,pocet hodin jedneho dna a pocet miest: ").split()
        if self.checking(self.initial) != "Prepracovat":
            for i in range(int(self.initial[2])*2):
                numbers = input("Zadajte hranice pasiem: ").split()
                if self.checking(numbers) != "Prepracovat":
                    self.bounds.append(numbers)
                else:
                    return "Prepracovat"
        else:
            return "Prepracovat"

        for _ in range(int(self.initial[3])):
            city = input("Zadajte polohu a nazov mesta: ").split()
            for badge in enumerate(city):
                if badge[0] <= 1:
                    if badge[1].isalpha():
                        return "Prepracovat"
                else:
                    if badge[1].isdigit():
                        return "Prepracovat"
            self.cities.append(city)
            self.seperated_cities.append(city[2])
                        
    def checking(self,numbers):
        for number in numbers:
            if number.isalpha():
                return "Prepracovat"
        if len(numbers)!=4:
            return "Prepracovat"            

class Main(Loading):
    def __init__(self):
        super().__init__()

    def checking_cities(self,find_out):
        for i in range(len(find_out[0])):
            if find_out[0][i].isdigit() or find_out[0][i] == ":":
                pass
            else:
                return "Prepracovat"
    
    def hlavny_cyklus(self,task=[],result=30,indexy=[]):
        finding_spaces = input("Zadajte pocet hladanych pasiem: ").strip()
        for _ in range(int(finding_spaces)):
            finding_city = input("Zadajte cas a 2 mesta: ").split()
            if self.checking_cities(finding_city) == "Prepracovat" or len(finding_city)!= 3 or \
               finding_city[1] not in self.seperated_cities or finding_city[2] not in self.seperated_cities:
                return "Prepracovat"
            task.append(finding_city)
            
        for i in range(len(task)):             
            my_time = task[i][0]
            if int(self.cities[self.seperated_cities.index(task[i][1])][0]) <= int(self.cities[self.seperated_cities.index(task[i][2])][0]):
                result *= int(self.cities[self.seperated_cities.index(task[i][2])][0])//(2*int(self.initial[2]))-1
                minutes = int(my_time[0:2])*60 + int(my_time[3:5]) + result
                print(time.strftime("%M:%S", time.gmtime(minutes)))
            else:
                result *= int(self.cities[self.seperated_cities.index(task[i][2])][0])//(2*int(self.initial[2]))
                if int(my_time[3:5]) - 30 > 0:
                    real_time = int(my_time[3:5]) - 30
                else:
                    real_time = int(my_time[3:5]) 
                minutes = real_time + result
                print(time.strftime("%M:%S", time.gmtime(minutes)))
            result = 30
        return "End"
                       
    def __str__(self):
        if self.enquiry() != "Prepracovat":
            return str(self.hlavny_cyklus())
        else:
            return "Prepracovat"

cyklus = input("Zadajte pocet cyklov: ").strip()
if cyklus.isdigit() and len(cyklus)>=1:
    while int(cyklus)!=0:
        print(Main())
        cyklus = int(cyklus)-1 
else:
    print("Nezadali ste cislo!")












