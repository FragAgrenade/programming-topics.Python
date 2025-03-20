number = int(input("Digite um número inteiro: "))

if number <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    print(f"Os divisores de {number} são:")

    for i in range(1, number + 1):
        if number % i == 0:
            print(i)