"""
import random
from unidecode import unidecode

with open('lista_palavras (1).txt', encoding='utf-8', mode='r') as arquivo:
	linhas = arquivo.readlines()

#remove todos os acentos das palavras
palavras_sem_acentos = [unidecode(palavra) for palavra in linhas]

#armazena apenas palavras de 5 letras
palavras = []
for palavra in palavras_sem_acentos:
	palavra = palavra.strip('\n')
	if len(palavra) == 5:
		palavras.append(palavra)
		
print(palavras)

#101 palavras


sorteio = random.randint(0, 101)
palavra_sorteada = palavras[sorteio]

print(palavra_sorteada)

palpite = input("Digite uma palavra: ")

for letra in palpite:
	if letra in palavra_sorteada:
		indice = palavra_sorteada.index(letra)
		print(f"indice {indice}")

"""

import random
from unidecode import unidecode



# Função para escolher uma palavra aleatória do arquivo com 5 letras (sem acentos)
def escolher_palavra():
    with open('lista_palavras (1).txt', encoding='utf-8', mode='r') as arquivo:
	    linhas = arquivo.readlines()

    sem_acento = [unidecode(palavra) for palavra in linhas]

    palavras = []
    for palavra in sem_acento:
	    palavra = palavra.strip('\n')
	    if len(palavra) == 5:
		    palavras.append(palavra)
		
    return random.choice(palavras)

escolher_palavra()

# Função para mostrar a palavra com letras adivinhadas
def mostrar_palavra(palavra, letras_adivinhadas):
    resultado = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

# Função principal do jogo
def jogar_forca():
    palavra = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 6

    print(palavra)
    print("Bem-vindo ao jogo da Forca!")
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


jogar_forca()