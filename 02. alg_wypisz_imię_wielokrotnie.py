from time import sleep

print("Program wypisuje zadane imię zadaną ilość razy")
imie=input("Podaj imię: ")
ilosc=int(input("Podaj, ile razy ma być wypisane: "))
if ilosc<=0:
    print("Podano niewłaściwą ilość powtórzeń")
else:
    for i in range(ilosc):
        print(imie)
sleep(5)
