nota1 = float(input('Digite a primera nota do aluno: '))
nota2 = float(input('Diginte a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print('Tirando {} e {} a media do aluno é {}'.format(nota1,nota2,media))
if media >= 7:
    print('O aluno foi aprovado!')
elif media < 7:
    print('O aluno foi reprovado.')
