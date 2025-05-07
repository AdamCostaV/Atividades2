# oitava questão
valor1 = int(input("Digite um número "))
valor2 = int(input("Digite outro número "))
valor3 = int(input("Digite mais um número "))
suporte = str(valor1 )  + str(valor2 )  + str(valor3)
ordenada = sorted(suporte, reverse=True)
print("Ordem decrescente:", ordenada)