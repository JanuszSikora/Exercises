from time import sleep
from math import sqrt
print("Program oblicza pole trójkąta po podaniu jego 3 boków a,b,c")
a=float(input("Podaj bok a: "))
b=float(input("Podaj bok b: "))
c=float(input("Podaj bok c: "))
p=(a+b+c)/2
if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a:
    print("Z takich boków nie można zbudować trójkąta")
else:
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    print("Pole trójkąta to: ",s)
sleep(5)
