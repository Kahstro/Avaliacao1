def tinta():
	metrosQ=int(input('Metros quadrados:'))
	litros=(1/3)*metrosQ
	litros=int(litros)
	if (litros*3)!=metrosQ:
		litros=litros+1
	lata=litros/18
	lata=int(lata)
	if (lata*18)!=litros:
		lata=lata+1
	return print('Latas: %d\nPreco: %d R$'%(lata,lata*80))
