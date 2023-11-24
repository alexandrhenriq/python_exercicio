# 2) Implementar uma função que retorne uma mensagem de boas-vindas, a partir de um nome de aluno. 

def mensagem_boas_vindas(nome_aluno):
    mensagem = f"Seja bem-vindo {nome_aluno}!"
    return mensagem

nome_do_aluno = (input("Informe seu nome: "))
boas_vindas = mensagem_boas_vindas(nome_do_aluno)
print(boas_vindas)
