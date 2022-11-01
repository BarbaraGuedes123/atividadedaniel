from logging import raiseExceptions


num:int;valoQuadrado:float;valoCubo:float;raiz:float

num=0
valoQuadrado=0
valoCubo=0
raiseExceptions=0

num=int(input("Digite um número: "))

for n in range(1,4):
    print(num ^2)
    print(num ^3)
    