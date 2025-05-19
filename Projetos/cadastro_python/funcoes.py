def exibir_apresentacao():
    print("Bem-vindo(a) ao Sistema de Cadastro")

def exibir_menu_opcoes():
    print("\n1- Cadastrar Usuário no Sistema\n"
          "2- Verificar Cadastro de Usuário\n"
          "3- Excluir Cadastro de Usuário\n"
          "4- Exibir Cadastro Completo do Sistema\n"
          "5- Atualizar Informação de Usuário\n"
          "6- Sair do Sistema\n")

def apresentacao_setor(opcao):
    match opcao:
        case 1: print("\n| Cadastrar Usuários no Sistema |\n")
        case 2: print("\n| Verificar Cadastro de Usuário |\n")
        case 3: print("\n| Excluir Cadastro de Usuário |\n")
        case 4: print("\n| Exibir Cadastro Completo do Sistema |\n")
        case 5: print("\n| Atualizar Informação de Usuário |\n")
        case 6: encerrar_aplicativo()
        case _: print("\nOpção inexistente\n")

def encerrar_aplicativo():
    print("Encerrando sistema...")
    print("Encerrado!")

def confirmacao_cadastro():
    print("\nO usuário foi cadastrado no sistema!\n")

def identifica_duplicata():
    print("\nUsuário já cadastrado!\n")

def retorna_menu():
    print("Retornando ao menu...")
