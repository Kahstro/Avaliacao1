def turno():
	turno=str(input('Em qual turno estudas?(M - Matutino, V - Vespertino ou N - Noturno)'))
	if turno=='M':
		print('Bom Dia!')
	elif turno=='V':
		print('Boa Tarde!')
	elif turno=='N':
		print('Boa Noite!')
	else: print('Valor Inválido!')
