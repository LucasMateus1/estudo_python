#função calculadora de média individual
def media_do_aluno (name, a, b): 
    nome = name
    notas = b
    quantidade_provas= b
    media = a/b
    print('A nota do aluno {} é {:.3f}'.format(nome, media))
#Variáveis
turma = []
contador = 0
alunoturma1 = float(input('Há quantos alunos em sua turma?'))
alunoturma = alunoturma1 + 1
#listagem de notas da turma
while True:
    contador += 1
    if contador == alunoturma:
        break
    else:
        print('')
        media_do_aluno(input('qual o nome do aluno?'), float(input('digite a soma de todas as notas do aluno:')), float(input('digite a quantidade de provas que o aluno realizou:')))
        print('')
        turma.append(float(input('digite a nota arredondada do aluno: ')))
        
#soma da Lista de notas da turma        
media = sum(turma) / alunoturma

#exibições finais
print('')

print('Notas dos alunos: {}'.format(turma))
if media >= 6:
    print('a média da turma é {:.2f}, parabéns!!!'.format(media))
else:
    print('a média da turma é {:.2f}, está abaixo do esperado!'.format(media))
#fim de código