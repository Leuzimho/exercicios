import random

def imprimir_tabuleiro(tabuleiro):
    """
    função que imprime o tabuleiro do jogo da velha NxN.

    argumentos:
        tabuleiro (list): uma matriz NxN representando o tabuleiro do jogo.
    """
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * (4 * len(linha) - 1))

def verificar_vitoria(tabuleiro, jogador):
    """
    função que verifica se um jogador venceu o jogo

    argumentos:
        tabuleiro (list): uma matriz NxN representando o tabuleiro do jogo
        jogador (str): o jogador a ser verificado ("X" ou "O")

    retorna:
        bool: True se o jogador venceu, False caso contrário
    """
    tamanho = len(tabuleiro)

    # Verificar linhas e colunas
    for i in range(tamanho):
        if all(tabuleiro[i][j] == jogador for j in range(tamanho)) or all(tabuleiro[j][i] == jogador for j in range(tamanho)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(tamanho)) or all(tabuleiro[i][tamanho - 1 - i] == jogador for i in range(tamanho)):
        return True

    return False

def jogar_jogo_da_velha():
    """
    função principal que permite ao jogador jogar o jogo da velha NxN contra a máquina
    """
    tamanho = int(input("Digite o tamanho do tabuleiro (NxN): "))
    tabuleiro = [[" " for _ in range(tamanho)] for _ in range(tamanho)]
    jogador_humano = "X"
    jogador_maquina = "O"
    jogadas = 0

    while True:
        imprimir_tabuleiro(tabuleiro)

        if jogadas % 2 == 0:
            jogador_atual = jogador_humano
            print("Sua vez!")
            linha = int(input(f"Informe a linha (0-{tamanho - 1}): "))
            coluna = int(input(f"Informe a coluna (0-{tamanho - 1}): "))
        else:
            jogador_atual = jogador_maquina
            print("Vez da máquina (O).")
            linha, coluna = jogada_maquina(tabuleiro, jogador_maquina)

        if 0 <= linha < tamanho and 0 <= coluna < tamanho and tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            jogadas += 1
        else:
            print("Jogada inválida. Tente novamente.")
            continue

        if jogadas >= tamanho * 2 - 1 and verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            if jogador_atual == jogador_humano:
                print("Você venceu!")
            else:
                print("A máquina venceu!")
            break
        elif jogadas == tamanho * tamanho:
            imprimir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

def jogada_maquina(tabuleiro, jogador_maquina):
    """
    função que representa a jogada da máquina (jogador "O") como um movimento aleatório

    args:
        tabuleiro (list): uma matriz NxN representando o tabuleiro do jogo
        jogador_maquina (str): jgoada da máquina ("O")

    retorna:
        tupla: coordenadas da jogada da máquina.
    """
    tamanho = len(tabuleiro)
    while True:
        linha = random.randint(0, tamanho - 1)
        coluna = random.randint(0, tamanho - 1)
        if tabuleiro[linha][coluna] == " ":
            return linha, coluna


print("Bem-vindo ao Jogo da Velha NxN contra a máquina!")
jogar_jogo_da_velha()
