# 1) Implementar uma função para calcular o salário líquido de um funcionário, a partir de seu salário base,
# do bônus mensal (em %) e do total de descontos.
 
def calcular_salario_liquido(salario_base, bonus_percentual, descontos):
    bonus = salario_base * (bonus_percentual / 100)
    salario_bruto = salario_base + bonus
    salario_liquido = salario_bruto - descontos
    return salario_liquido

salario_base = int(input("Digite o salário base: "))
bonus_percentual = int(input("Digite o bônus percentual: "))
descontos = int(input("Digite o desconto: "))

salario_final = calcular_salario_liquido(salario_base, bonus_percentual, descontos)
print(f"O salário líquido do funcionário é: R$ {salario_final:.2f}")