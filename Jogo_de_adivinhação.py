import random

def jogo_adivinhacao():

    drawn_number = random.randint(1, 100)
    attempts = 0
    hit = False

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número que estou pensando, entre 1 e 100.")

    while not hit:
        guess = int(input("Digite seu palpite: "))
        attempts += 1

        if guess < drawn_number:
            print("O número que estou pensando é maior que", guess)
        elif guess > drawn_number:
            print("O número que estou pensando é menor que", guess)
        else:
            hit = True
            print(f"Parabéns! Você acertou o número {drawn_number} em {attempts} tentativas!")


jogo_adivinhacao()