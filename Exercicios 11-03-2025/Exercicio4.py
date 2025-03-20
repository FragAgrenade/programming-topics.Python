quantity_students = int(input("Digite a quantidade de alunos: "))

bellow_average = 0
on_average = 0

for i in range(quantity_students):
    nota = int(input(f"Digite a nota do {i + 1}º aluno (0 a 100): "))

    if nota < 60:
        bellow_average += 1
    else:
        on_average += 1

print(f"Quantidade de alunos abaixo da média: {bellow_average}")
print(f"Quantidade de alunos na média: {on_average}")