from time import sleep
print("Sprawdzam czy liczba naturalna a jest liczbą pierwszą")
a=-1
while a<0:
    a=int(input("podaj a: "))
    if a<0:
        print("Podaj liczbę naturalną")
if a==0 or a==1:
        print(a," to nie liczba pierwsza")
else:
    licz=2
    for i in range(2,a):
        if a%i!=0:
            licz=licz+1
    if licz==a:
        print(a," jest liczbą pierwszą")
    else:
        print(a," nie jest liczbą pierwszą")    
sleep (5)
 
