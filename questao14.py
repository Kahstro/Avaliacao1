def contaEV():
	frase=str(input('Frase: '))
	i=0
	x=0
	while i<len(frase):
		if frase[i]==' ':
			x=x+1
		i=i+1
	print('Espacos: %d'%(x))
	i=0
	x=0
	while i<len(frase):
		if frase[i]=='a' or frase[i]=='e' or frase[i]=='i' or frase[i]=='o' or frase[i]=='u':
			x=x+1
		i=i+1
	print('Vogais: %d'%(x))
