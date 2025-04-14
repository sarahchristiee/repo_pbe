
num = int(input("Digite um número inteiro positivo: "))
i=1
fator = 1

if num >=0:
    while i<=num:
        fator = fator * i
        i += 1

else:
    print("INVÁLIDO")

print(f"O fatorial de {num} é {fator}")