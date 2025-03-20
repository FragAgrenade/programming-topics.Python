import math

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))


delta = b**2 - 4 * a * c


if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"As raízes são reais e distintas: x1 = {x1:.2f}, x2 = {x2:.2f}")
elif delta == 0:

    x = (-b) / (2 * a)
    print(f"A equação possui uma raiz real dupla: x = {x:.2f}")
else:

    part_real = -b / (2 * a)
    part_imaginaria = math.sqrt(-delta) / (2 * a)
    print(f"As raízes são complexas: x1 = {part_real:.2f} + {part_imaginaria:.2f}i, x2 = {part_real:.2f} - {part_imaginaria:.2f}i")