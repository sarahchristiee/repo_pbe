n = int(input("Digite um número inteiro positivo: "))

quadrado = n ** 2
str_quadrado = str(quadrado)

for i in range(1, len(str_quadrado)):
    esquerda = int(str_quadrado[:i]) if str_quadrado[:i] else 0
    direita = int(str_quadrado[i:]) if str_quadrado[i:] else 0

    if esquerda + direita == n and direita != 0:
        print(f"{n} é um número de Kaprekar.")
        break
else:
    if n == 1:
        print("1 é um número de Kaprekar.")  # Exceção clássica
    else:
        print(f"{n} não é um número de Kaprekar.")