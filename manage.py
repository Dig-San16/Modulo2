#Título
print("/" * 30)
print("\033[0;33;40m        JOGO DA VELHA       \033[m")
print("/" * 30)
print("\n")

#Função que guarda todo o jogo
def Jogo():

    #Dicionário que guarda as posições
    tabela = {
            "1": " ", "2": " ", "3": " ",
                
            "4": " ", "5": " ", "6": " ",

            "7": " ", "8": " ", "9": " "
    }

    #Variáveis principais
    jogador = "X"
    jogadas = []
    venceu = False

    #Uma lista que guarda listas
    vencedor = [
        # Linhas
        ["1", "2", "3"], 
        ["4", "5", "6"], 
        ["7", "8", "9"], 

        # Colunas
        ["1", "4", "7"], 
        ["2", "5", "8"], 
        ["3", "6", "9"],

        # Diagonais
        ["1", "5", "9"], 
        ["3", "5", "7"] 
    ]

    #O tabuleiro
    def tabuleiro():
        print("\n")
        print("         |         |")
        print(f"    {tabela['1']}    |    {tabela['2']}    |    {tabela['3']}")
        print("         |         |")
        print("---------+---------+---------")
        print("         |         |")
        print(f"    {tabela['4']}    |    {tabela['5']}    |    {tabela['6']}")
        print("         |         |")
        print("---------+---------+---------")
        print("         |         |")
        print(f"    {tabela['7']}    |    {tabela['8']}    |    {tabela['9']}")
        print("         |         |")

    #Repetição principal
    while True:
        tabuleiro()

        #Condição caso todos os espaços foram preenchidos
        if len(jogadas) == 9:
            print('\n')
            print("\033[1;33;40mEMPATE\033[m")
            break

        #Ambiente do jogador
        print("\n")
        posição = input(f"jogador {jogador}, escolha a posição: ")
        print("\n")

        #Condição caso o jogador digite um espaço já preenchido
        if posição in jogadas:
            print("\033[1;33;40messe espaço ja foi usado\033[m")
            continue

        #Condição que preenche os espaços vazios e adiciona as posições escritas na lista "jogadas"
        if posição in tabela:
            tabela[posição] = jogador
            jogadas += posição
        #Condição que avisa para não digitar qualquer coisa diferente de 1 a 9.
        else:
            print("\033[1;33;40mDigite entre 1 ou 9 pls\033[m")
            print("\n")
            continue

        #Condição que identifica se há um vencedor
        for linha in vencedor:
            if tabela[linha[0]] == tabela[linha[1]] == tabela[linha[2]] != " ":
                venceu = True

        #Condição que mostra o vencedor
        if venceu:
            tabuleiro()
            print('\n')
            print(f"\033[1;32;40mJogador {jogador} venceu!\033[m") 
            break   

        #Condição que alterna entre jogadores a medida que a partida progride
        jogador = "O" if jogador == "X" else "X"

Jogo()

#Repetição do "deseja continuar?"
while True:
    print("\n")
    a = input("Deseja jogar novamente? (S/N): ").lower().strip()
    if a == "s":
        Jogo()
    elif a == "n":
        print("\033[1;33;40mTCHAU TCHAU!\033[m")
        break
    else:
        print("\033[1;31;40mDigite entre S ou N pls\033[m")