compra = float(input("Digite o valor do seu produto: "))
confirmar = float(input("Digite novamente o valor da compra: "))
print(str("Como vai ser afetuado o pagamento, tem a opção de pagar com pix ou com dinheiro que sai com um desconto de 15%, cartão de credito tem 10% de desconto, parcelado duas vezes é o preço normal sem juros e parcelado 3 vezes tem de 10% "))
print("Digite dinheiro ou pix ou credito ou parcelado2 ou parcelado3")
forma_de_pagamento = str(input("Forma de pagamento: "))
if forma_de_pagamento == ("dinheiro"):
    novo_valor = confirmar - compra * 0.15
if forma_de_pagamento == ("pix"):
    novo_valor = confirmar - compra * 0.15
if forma_de_pagamento == ("credito"):
    novo_valor = confirmar - compra * 0.10
if forma_de_pagamento == ("parcelado2"):
    novo_valor = compra
if forma_de_pagamento == ("parcelado3"):
    novo_valor = confirmar + compra * 0.10
print(f"Novo valor é {novo_valor}")