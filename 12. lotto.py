import random
from time import sleep
print("Lotto - zwraca 6 losowych liczb z zakresu 1-49")
lista=[0]*49
for i in range(49):
    lista[i]=i+1
print(random.sample(lista,6))
sleep (5)
 
