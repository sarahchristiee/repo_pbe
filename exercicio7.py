n = int(input("Digite um número inteiro: "))

linha = 1

while linha <= n:
    coluna = 1
    while coluna <= linha:
        print("*", end="")
        coluna += 1
    print("\n")
    linha += 1