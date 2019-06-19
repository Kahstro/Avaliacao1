def crime():
	resposta=str(input('Telefonou para a vitima?(S ou N)'))
	nivel=0
	if resposta=='S':
		nivel=nivel+1
	resposta=str(input('Esteve no local do crime?(S ou N)'))
	if resposta=='S':
		nivel=nivel+1
	resposta=str(input('Mora perto da vitima?(S ou N)'))
	if resposta=='S':
		nivel=nivel+1
	resposta=str(input('Devia para a vitima?(S ou N)'))
	if resposta=='S':
		nivel=nivel+1
	resposta=str(input('Ja trabalhou com a vitima?(S ou N)'))
	if resposta=='S':
		nivel=nivel+1
	if nivel==2:
		print('Suspeita')
	elif nivel==3 or nivel==4:
		print('Cumplice')
	elif nivel==5:
		print('Assassino')
	else:
		print('Inocente')
