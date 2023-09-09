import random
from unidecode import unidecode

# Função para escolher uma palavra aleatória do arquivo com 5 letras (sem acentos)
def escolher_palavra():
    # Abre o arquivo "lista_palavras.txt" no modo de leitura com codificação UTF-8
    with open('lista_palavras (1).txt', encoding='utf-8', mode='r') as arquivo:
        # Lê todas as linhas do arquivo e armazena em uma lista chamada linhas
        linhas = arquivo.readlines()

    # Remove acentos de cada palavra no arquivo usando a biblioteca unidecode
    sem_acento = [unidecode(palavra) for palavra in linhas]

    # Cria uma lista vazia chamada palavras
    palavras = []
    
    # Itera pelas palavras sem acentos
    for palavra in sem_acento:
        # Remove caracteres de nova linha e espaços em branco no início e no final de cada palavra
        palavra = palavra.strip('\n')
        # Verifica se a palavra tem 5 letras
        if len(palavra) == 5:
            # Se tiver 5 letras, adiciona à lista de palavras
            palavras.append(palavra)
        
    # Retorna uma palavra aleatória da lista de palavras com 5 letras
    return random.choice(palavras)

# Função para mostrar a palavra com letras adivinhadas
def mostrar_palavra(palavra, letras_adivinhadas):
    resultado = ""
    # Itera pelas letras da palavra
    for letra in palavra:
        # Verifica se a letra está nas letras adivinhadas
        if letra in letras_adivinhadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

# Função principal do jogo
def jogar_forca():
    # Escolhe uma palavra aleatória
    palavra = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 6

    print("Jogo de Forca")
    print(f"Adivinhe a palavra: {mostrar_palavra(palavra, letras_adivinhadas)}")

    while tentativas > 0:
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite uma única letra válida.")
            continue

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra antes.")
            continue

        letras_adivinhadas.append(letra)

        if letra in palavra:
            print(f"Boa! A letra '{letra}' está na palavra: {mostrar_palavra(palavra, letras_adivinhadas)}")
        else:
            tentativas -= 1
            print(f"Letra '{letra}' não está na palavra. Tentativas restantes: {tentativas}")

        if "_" not in mostrar_palavra(palavra, letras_adivinhadas):
            print("Parabéns! Você adivinhou a palavra!")
            break

    if tentativas == 0:
        print(f"Você perdeu! A palavra era '{palavra}'.")

# Inicia o jogo chamando a função jogar_forca()
jogar_forca()
