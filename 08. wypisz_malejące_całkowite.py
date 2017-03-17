from time import sleep
print("Wypisuję liczby całk. od a do zera")
a=-1
while a<=0:
    a=int(input("podaj l. całk. a>0 "))
if a>0:
    for i in reversed(range(a+1)):
        print(i,end=" ")
sleep (5)
 
