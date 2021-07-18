#Função que calcula as notas individuais

def nota_individual(quantidade_de_notas):
	quantidade_de_notas = quantidade_de_notas
	cont = 0
	cont2 = 0
	notas =[]
	while True:
		cont2 += 1
		if cont2 > quantidade_de_notas:
			break
		else:
			cont += 1
			notaAnota = float(input('Digite a nota {} do aluno: '.format(cont)))
			notas.append(notaAnota)
			soma = sum(notas)
			media = soma / quantidade_de_notas
	print('notas: {}'.format(notas))
	print('A média do aluno foi: {:.2f}'.format(media))
	
#comando que analisa as notas da turma em geral
#explicação do programa
print('Antes de iniciarmos, deixe-me dar uma breve explicação...')
print('')
print('o programa funcionará da seguinte forma:')
print('')
print('primeiramente, o software irá fazer o calculo das notas individuais, aluno por aluno, após, o professor irá dar uma nota arredondada, podendo considerar pontos extras por aluno, ou até mesmo tirar pontos. assim será feita a listagem das médias de todos, tendo uma consideração final da média geral da turma...')
print ('')
input('Tecle enter para continuar...')
print('')
#início do codigo
turma = []
cont = 0
alunos = float(input('Há quantos alunos na turma? '))
while True:
	cont += 1
	if cont > alunos:
		break
	else:
		print ('')
		resposta = float(input('O aluno {} tem quantas notas? '.format(cont)))
		nota_individual(resposta)
		print('')
		arredondada = float(input('Digite a nota arredondada do aluno: '))
		turma.append(arredondada)

#comando que faz as printagens funais		
						
soma = sum(turma)
media = soma / alunos

print('')
print('Notas da turma: {}'.format(turma))
print('Média da turma: {:.2f}'.format(media))
if media >= 6:
	print('Parabéns, a média da turma está boa professor! :)')
else:
	print('A média da turma está abaixo do desejado professor :( ')
	#fim de código