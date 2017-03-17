
from time import sleep
import random
print("Sortuję listę o zadanej długości 'a', składającą się z losowych elementów int")
a=0
while a<=0:
    a=int(input("podaj a: "))

lista=[]
for el in range(a):
    lista.append(random.randint(-999,999))
print("lista nieposortowana",lista)

for i in range(len(lista)):
    for j in range(i + 1,len(lista)):
        if lista[i] > lista[j]:
            lista[i],lista[j]=lista[j],lista[i]
print("lista posortowana",lista)

sleep (5)
