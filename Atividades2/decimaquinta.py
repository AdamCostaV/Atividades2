from datetime import date
ano_nascimento = int(input("Digite o ano que você nasceu: "))
ano_atual = date.today().year
idade_anos = ano_atual - ano_nascimento
dias_totais = idade_anos * 365
anos = dias_totais // 365
resto = dias_totais % 365
meses = resto // 30
dias = resto % 30
print(f"Você já viveu {anos}, anos, {meses}, meses e {dias} dias ")