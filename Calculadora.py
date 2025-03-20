import math
operators = ["0 - sair","1 - subitração","2 - soma","3 - divisão","4 - potência","5 - mutiplicação","6 - raiz"]
result = 0

while True:

 print("Escolha a Operação desejada:")
 for op in operators:
    print(op)
 choice = input("Digite a operação desejada:")

 if choice not in ["0","1","2","3","4","5","6"]:
    print("Operação Invalida")


 else:

    if choice == "6":
          num1r = float(input("Digite o número: "))
          result = math.sqrt(num1r)
          print(f"Resultado: {result}")

    elif choice == "1":
          num1 = float(input("Digite o primeiro número: "))
          num2 = float(input("Digite o segundo número: "))
          result = num1 - num2
          print(f"Resultado: {result}")

    elif choice == "2":
          num1 = float(input("Digite o primeiro número: "))
          num2 = float(input("Digite o segundo número: "))
          result = num1 + num2
          print(f"Resultado: {result}")


    elif choice == "3":
          num1 = float(input("Digite o primeiro número: "))
          num2 = float(input("Digite o segundo número: "))
          result = num1 / num2 if num2 != 0 else "Erro, divisão por zero"
          print(f"Resultado: {result}")

    elif choice == "4":
          num1 = float(input("Digite o número: "))
          num2 = float(input("Digite o expoente: "))
          result = num1 ** num2
          print(f"Resultado: {result}")

    elif choice == "5":
          num1 = float(input("Digite o primeiro número: "))
          num2 = float(input("Digite o segundo número: "))
          result = num1 * num2
          print(f"Resultado: {result}")
    elif choice == "0":
          break
