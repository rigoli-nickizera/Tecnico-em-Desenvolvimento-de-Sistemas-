valorCompra = float(input("Digite o valor da sua compra:"))
cupomDesconto = input("Possui cupom de desconto?")

if(valorCompra >= 200 or cupomDesconto == "Sim"):
    print("Você ganhou um cupom de 15%!")
else:
    print("Você não tem direito a descontos no momento!")