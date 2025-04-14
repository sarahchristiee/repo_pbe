n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))


a = 0
b = 1

contador = 0

while contador < n:
    print(a, end=' ')
    a, b = b, a + b
    contador += 1