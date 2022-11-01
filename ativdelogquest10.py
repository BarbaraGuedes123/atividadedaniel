import math


somapares:int
num:int;somaprimos:int;contPrimo:int

contPrimo=0
somapares=0
somaprimos=0

for n in range(1,11):
    num=int(input("Digite um numero: "))
    if num % 2 == 0:
        somapares += num
    for m in range (1,num):
        if num % m == 0 :
            somapares += num

        for m in range(1,int(math.sqrt(num)+1)):
            if num % m == 0:
                contPrimo += 1

            if contPrimo == 0:
                somaprimos += num

print(f"Soma dos números pares: {somapares}")
print(f"Soma dos números primos: {somaprimos}")