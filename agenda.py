def menu():
    mostrarMenu = 's'
    while mostrarMenu == 's':
        opcao = input('''
_______________________________________________________________________________
|     PROJETO AGENDA - MONIQUE PARENTE | LINGUAGEM DE PROGRAMAÇÃO: PYTHON.    |
|                                                                             |
|                MENU:                                                        |
|                [1] CADASTRAR CONTATO.                                       |
|                [2] LISTAR CONTATO.                                          |
|                [3] DELETAR CONTATO.                                         |
|                [4] PESQUISAR CONTATO.                                       |
|                [5] ATUALIZAR CONTATO                                        |
|                [6] SAIR                                                     |
|                                                                             |
|_____________________________________________________________________________|
  ESCOLHA UMA OPÇÃO ACIMA:
  ''')
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            deletar()
        elif opcao == "4":
            pesquisar()
        elif opcao == '5':
            atualizar()
        else:
            sair()
        mostrarMenu = input("Voltar ao menu? (s/n) ").lower()

def cadastrar():
    idContato = input("ID: ")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f'{idContato};{nome};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso !!!!')
    except:
        print("ERRO na gravação do contato")


def listar():
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()


def deletar():
    nomeDeletado = input("Digite o nome para ser deletado: ").lower()
    agenda = open("agenda.txt", "r")
    listaTotal = []
    listaAtualizada = []
    for i in agenda:
        listaTotal.append(i)
    for i in range(0, len(listaTotal)):
        if nomeDeletado not in listaTotal[i].lower():
            listaAtualizada.append(listaTotal[i])
    agenda = open("agenda.txt", "w")
    for i in listaAtualizada:
        agenda.write(i)
    print(f'contato deletado com sucesso')
    listar()


def pesquisar():
    nome = input(f'digite o nome a ser procurado: ').upper()
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        if nome in contato.split(";")[1].upper():
            print(contato)
    agenda.close()

def atualizar():
    nomeDeletado = input("Digite o nome para ser Atualizado: ").lower()

    agenda = open("agenda.txt", "r")

    listaTotal = []
    listaAtualizada = []

    for i in agenda:
        listaTotal.append(i)

    for i in range(0, len(listaTotal)):
        if nomeDeletado not in listaTotal[i].lower():
            listaAtualizada.append(listaTotal[i])

    agenda = open("agenda.txt", "w")

    for i in listaAtualizada:
        agenda.write(i)

    idContato = input("ID para atualizar: ")
    nome = input("Nome para atualizar: ")
    telefone = input("Telefone para atualizar: ")
    email = input("Email para atualizar: ")

    try:
        agenda = open("agenda.txt", "a")

        dados = f'{idContato};{nome};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()

        print(f'Contato Atualizado com sucesso !!!!')
    except:
        print("ERRO na gravação do contato")

def sair():
    print(f'Até logo!! :D')
    exit()


def main():
    menu()


main()
