def numeroPNZ():
	numero=float(input('Numero: '))
	if numero<0:
		return 'N'
	elif numero>0:
		return 'P'
	else:
		return 'Z'
