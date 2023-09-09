import random

def imprimir_tabuleiro(tabuleiro):
    """
    função que imprime o tabuleiro do jogo da velha 4x4

    argumentos:
        tabuleiro (list): uma matriz 4x4 representando o tabuleiro do jogo
    """
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 29)

def verificar_vitoria(tabuleiro, jogador):
    """
    função que verifica se um jogador venceu o jogo

    argumentos:
        tabuleiro (list): uma matriz 4x4 representando o tabuleiro do jogo.
        jogador (str): o jogador a ser verificado ("X" ou "O")

    retorno:
        bool: true se o jogador venceu, False caso contrário
    """
    for i in range(4):
        if all(tabuleiro[i][j] == jogador for j in range(4)) or all(tabuleiro[j][i] == jogador for j in range(4)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(4)) or all(tabuleiro[i][3 - i] == jogador for i in range(4)):
        return True

    return False

def jogar_jogo_da_velha():
    """
    função principal que permite que o jogador jogue contra a máquina no jogo da velha 4x4
    """
    tabuleiro = [[" " for _ in range(4)] for _ in range(4)]
    jogador_atual = "X"
    jogadas = 0

    while True:
        imprimir_tabuleiro(tabuleiro)

        if jogador_atual == "X":
            print("Sua vez!")
            linha = int(input("Informe a linha (0-3): "))
            coluna = int(input("Informe a coluna (0-3): "))
        else:
            print("Vez da máquina (O).")
            linha, coluna = jogada_maquina(tabuleiro)

        if 0 <= linha < 4 and 0 <= coluna < 4 and tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            jogadas += 1
        else:
            print("Jogada inválida. Tente novamente.")
            continue

        if jogadas >= 4 and verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            if jogador_atual == "X":
                print("Você venceu!")
            else:
                print("A máquina venceu!")
            break
        elif jogadas == 16:
            imprimir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

def jogada_maquina(tabuleiro):
    """
    função que representa a jogada da máquina como um movimento aleatório

    argumentos:
        tabuleiro (list): Uma matriz 4x4 representando o tabuleiro do jogo

    retorno:
        tupla: coordenadas da jogada da máquina
    """
    while True:
        linha = random.randint(0, 3)
        coluna = random.randint(0, 3)
        if tabuleiro[linha][coluna] == " ":
            return linha, coluna
        

print("Bem-vindo ao Jogo da Velha 4x4 contra a máquina!")
jogar_jogo_da_velha()