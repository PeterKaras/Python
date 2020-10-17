def hlavny_cyklus(self,vysledok=""):
        for i in range(self.znamosti):
            if self.field[i][0] in self.library:
                for cislo in self.library[self.field[i][0]]:
                    if int(self.field[i][1]) > int(cislo):
                        break
                    else:
                        if int(self.field[i][0]) <= int(self.field[i][1]):
                            vysledok += str(self.field[i][0]) + " "
                            vysledok = self.prechadzanie(vysledok,cislo,i)
                        else:
                            vysledok += str(self.field[i][1]) + " "
                            vysledok = self.prechadzanie(vysledok,self.field[i][0],i)
                        self.library.setdefault(self.field[i][0],[]).append(self.field[i][1])
                        self.zoradenie(i)
                        break
            else:
                self.library.setdefault(self.field[i][0],[]).append(self.field[i][1])
                if int(self.field[i][0]) <=int(self.field[i][1]):
                    vysledok += str(self.field[i][0]) + " "
                else:
                    vysledok += str(self.field[i][1]) + " "
        vysledok = self.konecna(vysledok.split())
        return vysledok
