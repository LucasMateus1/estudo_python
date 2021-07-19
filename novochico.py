#função que calcula porcentagem ganha em cima dos produtos

def porcentagem_lucro(custo, venda):
	custo = custo
	venda = venda
	lucro = venda - custo
	valorR3 = lucro * 100
	ganho = valorR3 / custo
	return ganho

#inicio do programa


produtos = []
cont = 0
porcentagens = []
quantidade_produto = float(input('Quantos produtos irá calcular? '))

while True:
	cont += 1
	if cont > quantidade_produto:
		break 
	else:
		print('')
		produto = str(input('Qual o produto que deseja analisar? '))
	paguei = float(input(f'Quanto você pagou no(a) {produto}? '))
	vendi = float(input(f'A quanto você vendeu o(a) {produto}? '))

#consideração final 

	ganhei = porcentagem_lucro(paguei, vendi)
	print ('')
	print(f'a porcentagem ganha em cima do(a) {produto} foi de {ganhei :.2f}%')
	print('')
	produtos.append(f'{produto} ->')
	produtos.append(f'{ganhei:.2f}%')
	porcentagens.append(ganhei)
	
somaDePorcentagem = sum(porcentagens)
media = somaDePorcentagem / quantidade_produto
print(f'Listagem de produtos/ lucro percentual: {produtos}')
print('')
print(f'A porcentagem média ganha nos produtos calculados foi de {media:.2f}%')