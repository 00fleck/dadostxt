import os

listadedados = []

def exibir_nome_do_programa():
    print("""
    ████╗████╗████╗████╗████╗████╗████╗████╗████╗████╗████╗████╗████╗████╗████╗████╗
    ██╔═╝╚═██║██╔═╝╚═██║██╔═╝╚═██║██╔═╝╚═██║██╔═╝╚═██║██╔═╝╚═██║██╔═╝╚═██║██╔═╝╚═██║
    ██║░░░░██║██║░░░░██║██║░░░░██║██║░░░░██║██║░░░░██║██║░░░░██║██║░░░░██║██║░░░░██║
    ██║░░░░██║██║░░░░██║██║░░░░██║██║░░░░██║██║░░░░██║██║░░░░██║██║░░░░██║██║░░░░██║
    ████╗████║████╗████║████╗████║████╗████║████╗████║████╗████║████╗████║████╗████║
    ╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝
    """)

def exibir_menu(): 
    print('----------------------------------------------')
    print('1. Adicionar informações.')
    print('2. Listar as informações.')
    print('3. Gerar arquivo .txt')
    print('4. Sair.\n')
    print('script feito pelo lunatico')
    print('----------------------------------------------')

def Finalizar_app ():
    exibir_subtitulo('App finalizado.')
    # os.system('cls')
    # os.system('clear')  comando no mac e possivelmente no linux
    # print('Finalizando o aplicativo')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def adicionar_dados():
    exibir_subtitulo('Coloque as informações: ')
    dados = input()
    listadedados.append(dados)
    print(f'Os {dados} foi inseridos corretamente.\n')
    voltar_ao_menu_principal()

def listar_dados():
    exibir_subtitulo('Listando as informações adicionadas.')

    for dados in listadedados:
        print(f'.{dados}')

    voltar_ao_menu_principal() 


def escolhendo_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                adicionar_dados()
            case 2:
                listar_dados()
            case 3:
                print('Gerando o arquivo...')
            case 4:
                Finalizar_app()
            case _:
             opcao_invalida()
    except:
        opcao_invalida()      


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_menu()
    escolhendo_opcao()
    

if __name__ == '__main__':
    main()