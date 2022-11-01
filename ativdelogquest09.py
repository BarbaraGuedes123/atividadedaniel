from ast import If
import os

idade:int;somaIdade:int;pesoSuperior90alturaInferior150:int;idade10e30Altura190:int;peso:float;
altura:float;mediaIdade:float

pesoSuperior90alturaInferior150=0
somaIdade=0
idade10e30Altura190=0
peso=0
altura=0
mediaIdade=0
idade=0
 

for n in range(1,11):
    print(f"dados para {n} ª pessoa: ")
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso: "))
    altura = int(input("Digite a altura: "))
 
    os.system("cls")
    somaIdade  = somaIdade + idade
    if (peso > 90) and (altura < 1.50):
        pesoSuperior90alturaInferior150 +=1
    if(idade >= 10 and idade <= 30) and altura > 1.90:
        idade10e30Altura190 += 1

mediaIdade = somaIdade / 10

print(f"Média das idades das 10 pessoas: {mediaIdade: .2f}")
print(
     f"Quantidade de pessoas com peso superior a 90 kg e altura de 1.50: ")
print(
    f"porcentagem de pessoas que medem mais de 1,90 m: {idade10e30Altura190/10*100: .1f}%.")



  