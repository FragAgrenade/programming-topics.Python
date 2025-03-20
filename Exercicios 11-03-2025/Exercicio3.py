a = []

for i in range(10):
    number = int(input(f"Digite o {i + 1}º número inteiro: "))
    a.append(number)

major = max(a)
minor = min(a)

print("Lista de números armazenados:", a)
print(f"O maior número digitado foi: {major}")
print(f"O menor número digitado foi: {minor}")