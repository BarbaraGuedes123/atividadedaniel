idade: int
somaIdade: int
contIdade: int
mediaIdades: float

idade = 1
somaIdade = 0
contIdade = 0
mediaIdades = 0.0

while idade != 0:
    idade = int(input("Informe sua idade: "))

    somaIdade += idade
    contIdade += 1

mediaIdades = somaIdade / (contIdade - 1)

print("A Média das idade informadas: ", mediaIdades)