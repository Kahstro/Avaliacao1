def leet():
	texto=list(input('Texto: '))
	i=0
	traduzir=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	traduzido=['4','8','(','|)','3','|>|-|','9','|-|','|','_|','|<','|_','|\/|','|\|','0','|>','Q','.-','2','7','|_|','\/','\|/','><','`/','2']
	while i<len(texto):
		x=0
		while x<len(traduzir):
			if texto[i]==traduzir[x]:
				texto[i]=traduzido[x]
			x=x+1
		i=i+1
	textoT=''
	j=0
	while j<len(texto):
		textoT=textoT+texto[j]
		j=j+1
	print ('%s'%(textoT))
