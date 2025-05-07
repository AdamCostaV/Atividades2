# Setima questão
valor1 = int(input("Digite o primeiro valor (1 para Verdadeiro, 0 para Falso): "))
valor2 = int(input("Digite o segundo valor (1 para Verdadeiro, 0 para Falso): "))
if valor1 == 1 and valor2 == 1:
    print("Ambos são VERDADEIROS")
elif valor1 == 0 and valor2 == 0:
    print("Ambos são FALSOS")
else:
    print("Os valores são DIFERENTES (um verdadeiro e outro falso)")