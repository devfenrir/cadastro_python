import json
import funcoes
import os

opcao_digitada = -1

CAMINHO_ARQUIVO = "C:\\Users\\Felipe\\Desktop\\Projetos\\cadastro_python\\cadastro_sistema.txt"

if __name__ == "__main__":

    if os.path.exists(CAMINHO_ARQUIVO) and os.path.getsize(CAMINHO_ARQUIVO) > 0:
        with open(CAMINHO_ARQUIVO, "r", encoding="UTF-8") as arquivo:
            usuarios_cadastrados_sistema = json.load(arquivo)
    else:
        usuarios_cadastrados_sistema = {}

    while opcao_digitada != 6:

        funcoes.exibir_apresentacao()
        funcoes.exibir_menu_opcoes()

        try:
            opcao_digitada = int(input("Digite uma opção: "))
        except:
            print(f"Você inseriu um valor inválido\n")

        match opcao_digitada:
            case 1:
                funcoes.apresentacao_setor(1)

                nome_digitado = input("Digite o nome completo do usuário: ").strip()

                if nome_digitado in usuarios_cadastrados_sistema:
                    funcoes.identifica_duplicata()
                else:
                    email_digitado = input("Digite o email do usuário: ")
                    celular_digitado = input("Digite o celular do usuário: ")
                    profissao_digitada = input("Digite a profissão do usuário: ")

                    usuarios_cadastrados_sistema[nome_digitado] = {
                        "Nome": nome_digitado,
                        "Email": email_digitado,
                        "Celular": celular_digitado,
                        "Profissão": profissao_digitada
                    }

                    funcoes.confirmacao_cadastro()

                    with open(CAMINHO_ARQUIVO, "w", encoding="UTF-8") as arquivo:
                        json_string = json.dumps(usuarios_cadastrados_sistema, indent=4, ensure_ascii=False)
                        arquivo.write(json_string)

            case 2:
                funcoes.apresentacao_setor(2)

                consulta_nome = input("Digite o nome do usuário: ").strip()

                if consulta_nome in usuarios_cadastrados_sistema:
                    print(f"{consulta_nome} encontrado no sistema de cadastro!")
                    info = usuarios_cadastrados_sistema[consulta_nome]
                    print(f"Email: {info['Email']}")
                    print(f"Celular: {info['Celular']}")
                    print(f"Profissão: {info['Profissão']}")
                else:
                    print(f"{consulta_nome}, não encontrado no sistema!")

            case 3:
                funcoes.apresentacao_setor(3)

                consulta_usuario = input("Digite o nome do usuário: ").strip()

                if consulta_usuario in usuarios_cadastrados_sistema:
                    print(f"{consulta_usuario} encontrado no sistema de cadastro!")

                    procedimento = input("(S- sim ou N- não) Você deseja excluir o cadastro? ").strip().upper()

                    match procedimento:
                        case "S":
                            print(f"{consulta_usuario}, está sendo deletado do sistema...")
                            usuarios_cadastrados_sistema.pop(consulta_usuario)

                            with open(CAMINHO_ARQUIVO, "w", encoding="UTF-8") as arquivo:
                                json_string = json.dumps(usuarios_cadastrados_sistema, indent=4, ensure_ascii=False)
                                arquivo.write(json_string)

                        case "N":
                            funcoes.retorna_menu()

                        case _:
                            print(f"{procedimento}, é uma opção inválida!")

                else:
                    print(f"{consulta_usuario}, não encontrado no sistema!")

            case 4:
                funcoes.apresentacao_setor(4)

                if os.path.exists(CAMINHO_ARQUIVO) and os.path.getsize(CAMINHO_ARQUIVO) > 0:
                    with open(CAMINHO_ARQUIVO, "r", encoding="UTF-8") as arquivo:
                        print(arquivo.read())
                else:
                    print("Sistema de cadastro vázio até o momento...\n")
                    funcoes.retorna_menu()

            case 5:
                funcoes.apresentacao_setor(5)

                consulte_usuario = input("Digite o nome do usuário: ")

                if consulte_usuario in usuarios_cadastrados_sistema.keys():
                    novo_nome = input("Digite o novo nome do usuário: ")

                    email_novo = input("Digite o novo email: ")
                    celular_novo = input("Digite o novo celular: ")
                    profissao_nova = input("Digite a nova profissão: ")

                    usuarios_cadastrados_sistema.pop(consulte_usuario)

                    usuarios_cadastrados_sistema[novo_nome] = {
                        "Nome": novo_nome,
                        "Email": email_novo,
                        "Celular": celular_novo,
                        "Profissão": profissao_nova
                    }

                    with open(CAMINHO_ARQUIVO, "w", encoding="UTF-8") as arquivo:
                        json_string = json.dumps(usuarios_cadastrados_sistema, indent=4, ensure_ascii=False)
                        arquivo.write(json_string)

                else:
                    print("Usuário não cadastrado!")
                    funcoes.retorna_menu()

            case 6:
                funcoes.apresentacao_setor(6)