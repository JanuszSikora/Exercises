from time import sleep
print("Sprawdzam czy podana liczba naturalna a jest 3-narcystyczną liczbą Amstronga")

a=0
while a<=0:
    a=int(input("podaj a: "))
    if a<=0:
        print("Podaj liczbę naturalną")

s=0
licz=a
while licz>1:       #dopóki zostały jakieś cyfry
    s+=(int(licz%10))**3     #dodaj ostatnią cyfrę (jedności)
    licz/=10       #podziel liczbę przez 10
print ("suma: ",s) #wypisz sumę

if s==a:
    print(a," jest liczbą Amstronga")
else:
    print(a," nie jest liczbą Amstronga")    
sleep (5)
