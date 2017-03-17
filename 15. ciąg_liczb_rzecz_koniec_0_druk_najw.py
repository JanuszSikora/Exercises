from time import sleep
print("Zapamiętuję największą z podawanych liczb do podania zera i podaję największą")

a=-999999999999999999999
b=-999999999999999999999
while a!=0:
    a=float(input("podaj a: "))
    if a>b:
        b=a
        print("Największa podana liczba to: ",b)
sleep (5)
