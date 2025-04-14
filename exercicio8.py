n = int(input("Digite um número para soma harmônica: "))

soma = 0
i = 1

while i <= n:
    soma += 1 / i
    i += 1

print(f"A soma da série harmônica até {n} termos é: {soma:.2f}")
