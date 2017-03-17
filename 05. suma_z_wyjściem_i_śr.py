from time import sleep
from statistics import mean
print("Liczę sumę i średnią (jeżeli a i b>0 z a i b; jeśli podasz zero program się skończy")
a=b=1
while a!=0 and b!=0:
    a=float(input("Podaj a "))
    b=float(input("Podaj b "))
    if a==0 or b==0:
        print("Do widzenia")
    else:
        sum=a+b
        print("Suma to ",sum, end=", ")
        if a>0 and b>0:
            avg=mean([a,b])
            print("Średnia to ",avg)
        sleep (5)
else:
    sleep (1)
      
