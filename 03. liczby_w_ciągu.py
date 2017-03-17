from time import sleep
a=int(input("Podaj liczbę całk. >0; wypiszę liczby od zera do podanej wartości "))
if a<=0:
    print("Liczba ma być większa od zera")
else:
    for i in range(a+1):
        print(i,end=" ")
sleep (5)
      
