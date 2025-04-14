numero = 1
while numero <= 10000:
    soma_divisores = 0
    divisor = 1

    while divisor < numero:
        if numero % divisor == 0:
            soma_divisores += divisor
        divisor += 1

    if soma_divisores == numero:
        print(f"Números perfeitos entre 1 e 10000: {numero}")

    numero += 1