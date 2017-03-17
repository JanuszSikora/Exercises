from time import sleep
print("Sprawdzam czy podana liczba naturalna a jest liczbą doskonałą")
a=-1
while a<0:
    a=int(input("podaj a: "))
    if a<0:
        print("Podaj liczbę naturalną")
licz=0
for i in range(1,a):
    if a%i==0:
        licz=licz+i
if licz==a:
    print(a," jest liczbą doskonałą")
else:
    print(a," nie jest liczbą doskonałą")    
sleep (5)
 
