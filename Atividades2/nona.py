Peso = float(input("Coloque seu peso "))
Altura = float(input("Digite sua altura "))
imc = Peso / (Altura * Altura)
print(imc)
if imc <= 18.5: 
    print("Abaixo do peso ")
elif 18.6 < imc <= 24.9: 
    print("Peso ideal(Parabéns)")
elif 25.0 <= imc <= 29.9: 
    print("Levemente acima do peso")
elif 30.0 <= imc <= 34.9: 
    print("Obesidade grau I")
elif 35.0 <= imc <= 39.9:
    print("Obesidade grau II (severa)")
elif imc >= 40.0: 
    print("Obesidade grau III (mórbida)")
