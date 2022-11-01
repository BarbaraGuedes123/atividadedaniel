mpar:int;npar:int;soma:float;n:int
mpar=0
npar=0
n=0

mpar=int(input("Digite um valor para mpar: "))
npar=int(input("Digite um valor para npar: "))

while mpar >= npar:
    soma==0

    for n in range(1,n+1):
          soma=soma +n
    if mpar> npar:
          mpar+=1
          print(f"mpar e maior que npar")

    if npar < mpar:
        npar+=1
        print(f"npar não pode ser maior que mpar")

print(mpar>npar)
