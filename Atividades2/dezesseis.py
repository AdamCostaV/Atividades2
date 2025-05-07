lado1 = int(input("Digite o valor do primeiro  lado do triângulo: "))
lado2 = int(input("Digite o valor do segundo  lado do triângulo: "))
lado3 = int(input("Digite o valor do terceiro  lado do triângulo: "))
if lado1 == lado2 == lado3:
    print("Triângulo é Equilátero")
elif lado1 == lado2 != lado3:
 print("Triângulo é isósceles")
elif lado1 != lado2 == lado3:
    print("Triângulo é isósceles")
elif lado1 == lado3 != lado2:
     print("Triângulo é isósceles")
elif lado1 != lado2 != lado3:
    print("Triângulo é Escaleno")