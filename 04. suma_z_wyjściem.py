from time import sleep
print("Liczę sumę z a i b; jeśli podasz zero program się skończy")
a=b=1
while a!=0 and b!=0:
    a=float(input("Podaj a "))
    b=float(input("Podaj b "))
    if a==0 or b==0:
        print("Do widzenia")
    else:
        sum=a+b
        print("Suma to ",sum)
        sleep (5)
else:
    sleep (1)
      
