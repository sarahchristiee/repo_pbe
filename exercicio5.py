n = int(input("Digite um número inteiro: "))

divisores = 0
i = 1

while i <= n:
    if n % i == 0:
        divisores += 1
    i += 1

if divisores == 2:
    print(f"{n} é primo.")
else:
    print(f"{n} não é primo.")