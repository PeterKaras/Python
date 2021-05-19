import os
path = os.getcwd()
os.chdir(path)

class Main:
    def __init__(self):
        self.syms = {}
        self.counter = 0
        self.j = 1
        self.list_word = []
        
    def importing(self,command):
        with open("output.txt","a") as f:
            f.write(command)
        f.close()
            
    def append_more(self,key,words):
        for w in words:
            if w not in self.syms[key]:
                self.syms[key].append(w)
                  
    def load_syms(self,i,params):
        
        for word in params:
            word = word.split(" ")
            word[0] = word[0].lower()
            word[1] = word[1].lower()
            
            self.syms.setdefault(word[0],[]).append(word[0])
            
            if word[0] not in self.syms:
                self.syms.setdefault(word[0],[]).append(word[1])
            else:
                if word[1] not in self.syms[word[0]]:
                    self.syms[word[0]].append(word[1])
            
            if word[1] not in self.syms:
                self.syms.setdefault(word[1],[]).append(word[0])
            else:
                if word[0] not in self.syms[word[1]]:
                    self.syms[word[1]].append(word[0])
           
        
        for key in self.syms:
            for w in self.syms[key]:
                self.append_more(w,self.syms[key])
            
    def check_syms(self,i,params):
        for word in params:
            word = word.split(" ")
            word[0] = word[0].lower()
            word[1] = word[1].lower()
    
            if word[0] == word[1]:
                self.importing("synonyms\n")
            
            elif word[0] not in self.syms or word[1] not in self.syms:
                self.importing("different\n")
            
            elif word[0] in self.syms[word[1]] or word[1] in self.syms[word[0]]:
                self.importing("synonyms\n")
                
            else:
                self.importing("different\n")
        
    def main_loop(self,file):
        for i in range(int(file[0])):
            
            self.load_syms(file[self.j],file[self.j+1 : int(file[self.j])+self.j+1])
            self.j += int(file[self.j]) + 1
            #print(file[self.j])
            
            self.check_syms(file[self.j], file[self.j+1 : int(file[self.j])+self.j+1])
            self.j += int(file[self.j]) + 1
            #print(file[self.j])
            self.syms = {}
            
def read_file():
    with open("test.in","r") as f:
        file = f.read().split("\n")
    f.close()
    return file
    

if __name__ == "__main__":
    file = read_file()
    g = Main()
    g.main_loop(file)
    syms = g.syms