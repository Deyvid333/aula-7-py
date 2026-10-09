produto =" Mouse Gamer Wife"
valores = [20,71,100,30]

# pesquisa = input("pesquise um produto: ")
# if pesquisa == "Mouse".lower() in produto.lower():
#     print(produto)
# else:
#     print("Produto nao encontrado")


# escolha = int(input("digite um numero para saber o seu quadrado: "))

# def dobrar(escolha):
#     resultado = escolha * 2
#     return resultado

# # print(dobrar(escolha))

# valores_novos = []

# for item in valores:
#     valores_novos.append(dobrar(item))
 
# print(valores_novos)
# print(valores)

alunos = ["Ana", "Hugo", "Mariana", "Pedro", "Ana Paula"]

aluno_procurado = input("Pesquisar alunos pelo nome: ")
alunos_encontrados = []

for aluno in alunos:
    if aluno_procurado.lower() in aluno.lower():
        alunos_encontrados.append(aluno)
        

print(alunos_encontrados)