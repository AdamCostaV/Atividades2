nome = str(input("Digite seu nome "))
nota1 = float(input("Digite a Primeira nota "))
nota2 = float(input("Digite a Segunda nota "))
nota3 = float(input("Digite a Terceira nota "))
nota4 = float(input("Digite a Quarta nota "))
media = (nota1 + nota2 + nota3 + nota4)/4
if media >= 7: 
    print(f"O aluno {nome}, foi aprovado")
else: 
    print(f"O aluno {nome}, foi reporvado")