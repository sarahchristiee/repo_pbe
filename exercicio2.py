
num = int(input("Digite um número inteiro positivo: "))
i=1
soma = 0

if num >=0:
    while i<=num:
        soma += i
        i += 1

else:
    print("INVÁLIDO")

print(f"A soma de todos os números entre 1 e {num} é {soma}")
