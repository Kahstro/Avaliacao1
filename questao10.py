def login():
	usuario=str(input('Usuario:'))
	senha=str(input('Senha:'))
	while usuario==senha:
		print('Senha invalida')
		senha=str(input('Senha:'))
