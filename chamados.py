chamados = [
  { "id": 1, "titulo": "Erro no login", "prioridade": "Alta", "status": "Aberto", "usuario": "Ana Silva" },
  { "id": 2, "titulo": "Tela branca no app", "prioridade": "Crítica", "status": "Aberto", "usuario": "Bruno Costa" },
  { "id": 3, "titulo": "Atualizar cadastro", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Carlos Souza" },
  { "id": 4, "titulo": "Boleto não gerado", "prioridade": "Média", "status": "Aberto", "usuario": "Daniela Lima" },
  { "id": 5, "titulo": "Botão quebrado", "prioridade": "Baixa", "status": "Aberto", "usuario": "Eduardo Rocha" },
  { "id": 6, "titulo": "Lentidão na busca", "prioridade": "Média", "status": "Em progresso", "usuario": "Fernanda Alves" },
  { "id": 7, "titulo": "Recuperar senha", "prioridade": "Alta", "status": "Aberto", "usuario": "Gabriel Santos" },
  { "id": 8, "titulo": "Erro no Pix", "prioridade": "Crítica", "status": "Aberto", "usuario": "Amanda Melo" },
  { "id": 9, "titulo": "Mudar foto de perfil", "prioridade": "Baixa", "status": "Fechado", "usuario": "Igor Ribeiro" },
  { "id": 10, "titulo": "Exportar PDF falhou", "prioridade": "Média", "status": "Aberto", "usuario": "Juliana Vieira" },
  { "id": 11, "titulo": "Carrinho esvaziando", "prioridade": "Alta", "status": "Em progresso", "usuario": "Lucas Martins" },
  { "id": 12, "titulo": "Cupom inválido", "prioridade": "Média", "status": "Aberto", "usuario": "Mariana Dias" },
  { "id": 13, "titulo": "Página 404 no FAQ", "prioridade": "Baixa", "status": "Aberto", "usuario": "Nicolas Ferreira" },
  { "id": 14, "titulo": "Atraso na entrega", "prioridade": "Alta", "status": "Aberto", "usuario": "Patricia Gomes" },
  { "id": 15, "titulo": "Email de boas-vindas", "prioridade": "Baixa", "status": "Fechado", "usuario": "Rodrigo Ramos" },
  { "id": 16, "titulo": "Estorno pendente", "prioridade": "Alta", "status": "Em progresso", "usuario": "Sabrina Oliveira" },
  { "id": 17, "titulo": "Alerta de segurança", "prioridade": "Crítica", "status": "Aberto", "usuario": "Thiago Barbosa" },
  { "id": 18, "titulo": "Link quebrado no menu", "prioridade": "Baixa", "status": "Aberto", "usuario": "Vanessa Cunha" },
  { "id": 19, "titulo": "Nota fiscal sumiu", "prioridade": "Média", "status": "Aberto", "usuario": "Willian Cardoso" },
  { "id": 20, "titulo": "Modo escuro travando", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Yasmim Lopes" },
  { "id": 21, "titulo": "Erro na API de CEP", "prioridade": "Alta", "status": "Aberto", "usuario": "Arthur Antunes" },
  { "id": 22, "titulo": "Notificação duplicada", "prioridade": "Baixa", "status": "Aberto", "usuario": "Beatriz Mendes" },
  { "id": 23, "titulo": "Sessão expirando rápido", "prioridade": "Média", "status": "Em progresso", "usuario": "Caio Nogueira" },
  { "id": 24, "titulo": "Erro no cartão de crédito", "prioridade": "Crítica", "status": "Aberto", "usuario": "Diana Prince" },
  { "id": 25, "titulo": "Traduzir termo em inglês", "prioridade": "Baixa", "status": "Fechado", "usuario": "Elton John" },
  { "id": 26, "titulo": "Chat de suporte offline", "prioridade": "Alta", "status": "Aberto", "usuario": "Fábio Assunção" },
  { "id": 27, "titulo": "Upload de comprovante", "prioridade": "Média", "status": "Aberto", "usuario": "Gisele Bündchen" },
  { "id": 28, "titulo": "Histórico sumiu", "prioridade": "Alta", "status": "Em progresso", "usuario": "Heitor Villa" },
  { "id": 29, "titulo": "Termos de uso desatualizados", "prioridade": "Baixa", "status": "Aberto", "usuario": "Isabela Garcia" },
  { "id": 30, "titulo": "Erro 500 no checkout", "prioridade": "Crítica", "status": "Aberto", "usuario": "Jorge Ben" },
  { "id": 31, "titulo": "Ajustar margem do header", "prioridade": "Baixa", "status": "Em progresso", "usuario": "Karina Bacchi" },
  { "id": 32, "titulo": "Filtro por data quebrado", "prioridade": "Média", "status": "Aberto", "usuario": "Leonardo Dicaprio" },
  { "id": 33, "titulo": "Assinatura não renovada", "prioridade": "Alta", "status": "Aberto", "usuario": "Marta Vieira" },
  { "id": 34, "titulo": "Áudio do vídeo não funciona", "prioridade": "Média", "status": "Aberto", "usuario": "Neymar Junior" },
  { "id": 35, "titulo": "Atualizar política de privacidade", "prioridade": "Baixa", "status": "Fechado", "usuario": "Otávio Mesquita" },
  { "id": 36, "titulo": "Queda do servidor interno", "prioridade": "Crítica", "status": "Em progresso", "usuario": "Paula Toller" },
  { "id": 37, "titulo": "Convite por email falhou", "prioridade": "Baixa", "status": "Aberto", "usuario": "Quintino Aires" },
  { "id": 38, "titulo": "Extrato em branco", "prioridade": "Alta", "status": "Aberto", "usuario": "Renata Vasconcellos" },
  { "id": 39, "titulo": "ícone errado no painel", "prioridade": "Baixa", "status": "Aberto", "usuario": "Samuel Rosa" },
  { "id": 40, "titulo": "Duplicidade de cobrança", "prioridade": "Crítica", "status": "Aberto", "usuario": "Tais Araújo" },
  { "id": 41, "titulo": "Validação de CNPJ", "prioridade": "Média", "status": "Em progresso", "usuario": "Umberto Eco" },
  { "id": 42, "titulo": "Mensagem de erro confusa", "prioridade": "Baixa", "status": "Aberto", "usuario": "Valéria Valenssa" },
  { "id": 43, "titulo": "Problema com fonte negrito", "prioridade": "Baixa", "status": "Aberto", "usuario": "Wagner Moura" },
  { "id": 44, "titulo": "Links de redes sociais fora do ar", "prioridade": "Média", "status": "Aberto", "usuario": "Xuxa Meneghel" },
  { "id": 45, "titulo": "Sem sinal de geolocalização", "prioridade": "Alta", "status": "Em progresso", "usuario": "Yuri Gagarin" },
  { "id": 46, "titulo": "Página recarregando sozinha", "prioridade": "Alta", "status": "Aberto", "usuario": "Zeca Pagodinho" },
  { "id": 47, "titulo": "Gráfico de vendas travado", "prioridade": "Média", "status": "Aberto", "usuario": "Alinne Moraes" },
  { "id": 48, "titulo": "Impossível remover endereço", "prioridade": "Média", "status": "Em progresso", "usuario": "Beto Jamaica" },
  { "id": 49, "titulo": "Vazamento de memória na aba", "prioridade": "Crítica", "status": "Aberto", "usuario": "Cláudia Raia" },
  { "id": 50, "titulo": "Ajustar alinhamento do rodapé", "prioridade": "Baixa", "status": "Fechado", "usuario": "Dado Dolabella" }
]


print(" < Lista De Opçoes De Chamados > ")

print("digite: 1 para - pesquisar chamados por usuarios ")
print("digite: 2 para - pesquisar chamados por prioridade ")
print("digite: 3 para - pesquisar chamados por status ")
print("digite: 4 para - pesquisar chamados por urgentes ")
print("digite: 5 para - abrir um chamado ")
print("digite: 6 para - resolver um chamado ")
print("digite: 7 para - fechar um chamado ")
print("digite: 8 para - ver todas as opções ")
print("digite: 0 para - sair do sistema ")

def pesquisarPorUsuario():
  pesquisarUsuario = input("Digite o nome do usuario para averiguar o seu chamado: ")
  for chamado in chamados :
    if  pesquisarUsuario.lower() in chamado["usuario"].lower():
      print(chamado)

def pesquisarPorPrioridade():
  pesquisa = input("Digite a prioridade que voce deseja filtrar (Crítica/Alta/Média/Baixa): ")
  for chamado in chamados :
    if chamado["prioridade"].lower() == pesquisa.lower():
      print(chamado)

def pesquisarPorStatus():
  pesquisa = input("Digite o status que voce deseja filtrar(Aberto/Em progresso/Fechado): ")
  for chamado in chamados :
    if chamado["status"].lower() == pesquisa.lower():
      print(chamado)

def chamadasUrgentes():
  for chamado in chamados :
    if chamado["status"] == "Aberto" and chamado["prioridade"] == "Crítica" :
      print(chamado)

def abrirChamado():
  titulo_chamado = input("escreva o problema: ")
  prioridade_chamado = input("escreva a prioridade do probelma (Crítica/Alta/Média/Baixa): ")
  status_chamado = input("escreva o status da chamada (Aberto/Fechado/Em Progresso): ")
  usuario_chamado = input("escreva o seu nome: ")

  novo_chamado = {
    "id": len(chamados) + 1,
    "titulo": titulo_chamado,
    "prioridade": prioridade_chamado,
    "status": status_chamado,
    "usuario": usuario_chamado
  }
  chamados.append(novo_chamado)

def resolverChamado():
  pesquisarUsuario = input("Digite o nome do usuario para resolver o seu chamado: ")
  for chamado in chamados :
    if chamado["usuario"].lower() == pesquisarUsuario.lower():
      chamado["status"] = "Em Progresso"
      print(chamado)


def fecharChamado():
  pesquisarUsuario = input("Digite o nome do usuario para fechar o seu chamado: ")
  for chamado in chamados :
    if chamado["usuario"].lower() == pesquisarUsuario.lower():
      chamado["status"] = "Fechado"
      print(chamado)


def mostrarEscolhas():
  print(" < Lista De Opçoes De Chamados > ")

  print("digite: 1 para - pesquisar chamados por usuarios ")
  print("digite: 2 para - pesquisar chamados por prioridade ")
  print("digite: 3 para - pesquisar chamados por status ")
  print("digite: 4 para - pesquisar chamados por urgentes ")
  print("digite: 5 para - abrir um chamado ")
  print("digite: 6 para - resolver um chamado ")
  print("digite: 7 para - fechar um chamado ")
  print("digite: 8 para - ver todas as opções ")
  print("digite: 0 para - sair do sistema ")
  

while True:
  print("digite: 8 para - ver todas as opções ")
  escolha = int(input("Digite a opçao a ser executada porfavor : "))

  if escolha == 1 :
    pesquisarPorUsuario()

  elif escolha == 2 :
    pesquisarPorPrioridade()

  elif escolha == 3 :
    pesquisarPorStatus()

  elif escolha == 4 :
    chamadasUrgentes()

  elif escolha == 5 :
    abrirChamado()

  elif escolha == 6 :
    resolverChamado()

  elif escolha == 7 :
    fecharChamado()

  elif escolha == 8 :
    mostrarEscolhas()

  elif escolha == 0 :
    break

  else:
    print("Opção invalida digite novamente uma opção que seja valida da lista")
