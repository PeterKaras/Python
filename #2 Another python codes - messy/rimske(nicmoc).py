roman=input("Zadaj číslo v rímskej sústave: ")

values={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
numbers=[]
decimal=0

#Hodnotu každého znaku rímskeho čísla dám do nového poľa
for i in roman:
  numbers.append(values[i])

#Spočítam všetky prvky poľa
for i in range(len(roman)):
  decimal+=values[roman[i-1]]

#Ak je menší znak pred väčším (napr. IV), tak ho odčítam 2x, bo som ho predtým pričítal
for i in range(len(roman)):
  if numbers[i-1]<numbers[i] and i>0:
    decimal-=2*numbers[i-1]

print(numbers)
print(decimal)

"""
def roman_to_int(s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

print(roman_to_int("IM"))
"""
