# 3) Implementar uma função que retorne uma mensagem formatada com o valor das parcelas de uma
# compra, a partir do valor total da compra e da quantidade do parcelamento. 

def calcular_parcelas(valor_total, quantidade_parcelas):
    if quantidade_parcelas <= 0:
        return "Quantidade de parcelas inválida. Por favor, escolha um número positivo."

    valor_parcela = valor_total / quantidade_parcelas
    mensagem = f"Sua compra de R${total_compra:.2f} em {quantidade_parcelas}x de R${valor_parcela:.2f} foi concluída!"
    return mensagem

total_compra = int(input("Digite o total da compra: "))
parcelas = int(input("Digite a quantidade de parcelas: "))

mensagem_parcelas = calcular_parcelas(total_compra, parcelas)
print(mensagem_parcelas)
