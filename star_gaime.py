import time

def iniciar_jogo():
    print("\nCARREGANDO MISSÃO...\n")

    print("ANO: 2042")
    print("O Brasil está sob ameaça.")
    print("Uma potência inimiga está utilizando")
    print("códigos secretos para coordenar ataques.")

    print("\nVocê é o Agente 062.")
    print("Sua missão é descobrir as senhas.")

    input("\nPressione ENTER para continuar...")


def mostrar_creditos():
    print("\n=== CRÉDITOS ===")
    print("Desenvolvido pela Equipe Escudo Verde")
    print("Projeto Acadêmico")
    input("\nPressione ENTER para voltar...")


def menu_principal():
    while True:
        print("\n" + "=" * 40)
        print("      OPERAÇÃO ESCUDO VERDE")
        print("=" * 40)
        print("1 - Iniciar Missão")
        print("2 - Créditos")
        print("3 - Sair")
        print("=" * 40)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            iniciar_jogo()

        elif opcao == "2":
            mostrar_creditos()

        elif opcao == "3":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!\n")


print("Conectando aos servidores militares...")
time.sleep(2)

print("Verificando credenciais...")
time.sleep(2)

print("Acesso autorizado.")
time.sleep(1)

print("\nAGENTE 062 IDENTIFICADO")
time.sleep(2)

menu_principal()