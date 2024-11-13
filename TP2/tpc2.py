import random

# Modo compuador pensa e utilizador adivinha

def computador_pensa():
    print("Modo 1: O computador pensou em um número entre 0 e 100.")
    numero_secreto = random.randint(0, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        palpite = int(input("Tente adivinhar o número: "))
        tentativas = tentativas + 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            acertou = True
        elif palpite < numero_secreto:
            print("O número é maior.")
        else:
            print("O número é menor.")

# Modo utilizador pensa e computador adivinha 

def utilizador_pensa():
    print("Modo 2: Pense em um número entre 0 e 100 e o computador tentará adivinhar.")
    menor = 0
    maior = 100
    tentativas = 0
    acertou = False

    while not acertou:
        palpite = (menor + maior) // 2
        tentativas = tentativas + 1
        print(f"O computador acha que o número é {palpite}.")
        resposta = input("Digite 'c' se o computador acertou, 'm' se o número é maior, ou 'n' se é menor: ")

        if resposta == 'c':
            print(f"O computador acertou! O número é {palpite}. Tentativas: {tentativas}")
            acertou = True
        elif resposta == 'm':
            menor = palpite + 1
        elif resposta == 'n':
            maior = palpite - 1
        else:
            print("Resposta inválida. Digite 'c', 'm' ou 'n'.")

def escolher_modo():
    print("Bem-vindo ao jogo Adivinha o Número!")
    print("Escolha o modo de jogo:")
    print("1 - Computador pensa em um número e você tenta adivinhar")
    print("2 - Você pensa em um número e o computador tenta adivinhar")

    modo = input("Escolha o modo (1 ou 2): ")

    if modo == '1':
        computador_pensa()
    elif modo == '2':
        utilizador_pensa()
    else:
        print("Modo inválido. Por favor, escolha 1 ou 2.")

# Para iniciar o jogo
escolher_modo()