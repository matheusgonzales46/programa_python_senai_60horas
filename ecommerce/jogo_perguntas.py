banco_perguntas = [
'',
'Qual é o maior planeta do Sistema Solar?',
'Qual país tem o formato de uma bota?',
'Quantos continentes existem na Terra?'
]
respostas = [
'',
'jupiter',
'italia',
'sete',
]

print('JOGO DE PERGUNTAS ACERTE E GANHE 1 MILHÃO')
print('***' * 20)
maquina = random.choice(banco_perguntas)
id_maquina = banco_perguntas.index(maquina)
print(maquina)
print('***' * 20)

print('ESCOLHA SUA RESPOSTA')
r = int(input({respostas[1]}, {respostas[2]}, {respostas[3]}))

if r == id_maquina:
     print('acertou em cheio')
else:
     print('errou feio')
         
