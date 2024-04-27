import math
liczba1 = int(input("Podaj wartosc 1 liczby: "))
liczba2 = int(input("Podaj wartosc 2 liczby: "))
opcja = int(input("Wybierz opcje z menu: 1 - suma, 2 - roznica, 3 - iloczyn, 4 - iloraz, 5 - potegowanie, pierwiastkowanie - 6, pierwiastkowaniestp3 - 7,   "))

if opcja == 1:
    print("suma =", liczba1 + liczba2)
if opcja == 2:
    print("roznica =", liczba1 - liczba2)
if opcja == 3:
    print("iloczyn =", liczba1 * liczba2)
if opcja == 4:
    print("iloraz =", liczba1 / liczba2)  
if opcja == 5:
    print("potega =", liczba1 ** liczba2)    
if opcja == 6:
    print("pierwiastek =", math.sqrt(liczba1))
if opcja == 7:
    print("pierwiastek =", liczba1 ** (1/3))                 
if opcja !=1 and opcja !=2 and opcja !=3 and opcja !=4 and opcja !=5 and opcja !=6 and opcja !=7:
    print("Nie ma takiej opcji")  
