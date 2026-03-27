import random

# 1 - Criar um número aleatório entre 5 e 10

def numero_aleatorio_5_10():
    return random.randint(5, 10)


# 2 - Criar 3 números aleatórios

def tres_numeros_aleatorios():
    numeros = []
    for _ in range(3):
        numeros.append(random.randint(0, 100))
    return numeros


# 3 - Criar um número aleatório entre 10 e 30 usando range()

def numero_aleatorio_range():
    numeros = list(range(10, 31))  # 31 porque o range não inclui o último
    return random.choice(numeros)


# 4 - Contagem regressiva simples

def contagem_regressiva():
    for i in range(10, 0, -1):
        print(i)
    print("Fogo!")


# 5 - Soma de números pares 

def soma_pares(n):
    soma = 0
    for i in range(2, n + 1, 2):
        soma += i
    return soma


# ===== Testando as funções =====

print("1:", numero_aleatorio_5_10())

print("2:", tres_numeros_aleatorios())

print("3:", numero_aleatorio_range())

print("4:")
contagem_regressiva()

numero = int(input("Digite um número inteiro positivo: "))
print("5: Soma dos pares =", soma_pares(numero))
