print('sistema de verificação de media')

nome = input('digite o nome do aluno: ')

print('digite as notas do aluno:', nome)

n1 = float(input('digite sua nota 1 '))
n2 = float(input('digite sua nota 2 '))
n3 = float(input('digite sua nota 3 '))
print('***' * 15)
print('media do aluno(a) ', nome)
media = n1 + n2 + n3 / 3

print(media)

aprovado = media >= 7
recuperação = media >= media <7
reprovado = media <5

print(f'''
 situação da aluna {nome}     
aprovado?{aprovado}
reprovado?{reprovado}
recuperação?{recuperação}


''')




