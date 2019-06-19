def fruteira():
	morango=int(input('Quantidade (em Kg) de morangos:'))
	maca=int(input('Quantidade (em Kg) de macas:'))
	if (morango+maca)<=5:
		print('%f R$'%((morango*2.5)+(maca*1.8)))
	else:
		preco=(morango*2.2)+(maca*1.5)
		if (morango+maca)>8 or preco>25:
			print('%f R$'%(preco-preco*(10/100)))
		else:
			print('%f R$'%(preco))
