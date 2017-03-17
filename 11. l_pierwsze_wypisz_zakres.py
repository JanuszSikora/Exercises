from time import sleep
print("Wypisuje liczby naturalne z podanego zakresu a<=>b >=1")
a=-1
b=-1
while a<=1:
    a=int(input("podaj a: "))
while b<=1:
    b=int(input("podaj b: "))
for ln in range(a,b):
    licz=2        
    for i in range(2,ln):
        if ln%i!=0:
            licz=licz+1
    if licz==ln:
        print(ln,end=" ")
sleep (5)
 
