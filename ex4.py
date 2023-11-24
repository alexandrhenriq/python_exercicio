# 4) Implementar uma função que informe a classificação de um aluno a partir da média de 3 notas e da
# quantidade de faltas. O aluno já será considerado reprovado se a quantidade de faltas for maior que 30. A
# tabela abaixo apresenta as regras para os intervalos da média:
# Se a quantidade de faltas maior que 30 => Reprovado por falta
# Se média maior que 8 => Aprovado com sucesso
# Se média entre 6 e 8 => Aprovado
# Se média entre 3 e 5,9 => Recuperação
# Se média menor que 3 => Reprovado
# Se média igual a zero => Desistente

def classificar_aluno(media, faltas):
    # Verifica se a quantidade de faltas é maior que 30
    if faltas > 30:
        return "Reprovado por falta"

    # Verifica os intervalos da média
    if media == 0:
        return "Desistente"
    elif media > 8:
        return "Aprovado com sucesso"
    elif 6 <= media <= 8:
        return "Aprovado"
    elif 3 <= media < 6:
        return "Recuperação"
    elif media < 3:
        return "Reprovado"
    else:
        return "Classificação indefinida"

# Exemplo de uso da função
media_notas = 7.5
quantidade_faltas = 25

classificacao = classificar_aluno(media_notas, quantidade_faltas)
print(classificacao)
