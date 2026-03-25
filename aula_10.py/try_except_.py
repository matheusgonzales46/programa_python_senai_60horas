# AULA 11 TRY E EXCEPT:
#(ATIVIDADE 1):
print('atividade 1:')
try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número: {numero}")
except ValueError:
    print("Erro: você não digitou um número inteiro válido.")

#----------------------------
#(ATIVIDADE 2):
print('atividade 2:')
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = num1 / num2
    print(f"Resultado da divisão: {resultado}")
    
except ValueError:
    print("Erro: você deve digitar números válidos.")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")

#-----------------------------
# (ATIVIDADE 3):
print('atividade 3:')

lista = [10, 20, 30, 40, 50]

try:
    indice = int(input("Digite o índice da lista: "))
    print(f"Elemento no índice {indice}: {lista[indice]}")
    
except ValueError:
    print("Erro: você deve digitar um número inteiro para o índice.")
except IndexError:
    print("Erro: índice fora do alcance da lista.")

#-----------------------------------    



