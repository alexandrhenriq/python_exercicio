# 5) Implementar uma função que calcule o IMC de uma pessoa a partir do peso(kg) e altura(m) e informe a
# classificação.

def calcular_imc(peso, altura):
    # Verifica se os valores de peso e altura são válidos
    if peso <= 0 or altura <= 0:
        return "Valores inválidos para peso e/ou altura. Por favor, forneça valores positivos."

    # Calcula o IMC
    imc = peso / (altura ** 2)

    # Classifica o IMC
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        classificacao = "Peso normal"
    elif 25 <= imc < 29.9:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 34.9:
        classificacao = "Obesidade Grau I"
    elif 35 <= imc < 39.9:
        classificacao = "Obesidade Grau II"
    else:
        classificacao = "Obesidade Grau III"

    return f"Seu IMC é {imc:.2f}. Classificação: {classificacao}"

# Exemplo de uso da função
peso = 70
altura = 1.75

resultado_imc = calcular_imc(peso, altura)
print(resultado_imc)
