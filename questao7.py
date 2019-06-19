def aumento():
	salario=float(input('Salario:'))
	if salario<=280:
		salarioF=salario+(20/100*salario)
		pAumento=20
	elif salario>280 and salario<=700:
		salarioF=salario+(15/100*salario)
		pAumento=15
	elif salario>700 and salario<1500:
		salarioF=salario+(10/100*salario)
		pAumento=10
	else:
		salarioF=salario+(5/100*salario)
		pAumento=5
	return print ('Salario inicial: %f R$\nPercentual de aumento: %d\nValor do aumento: %f R$\nSalario final: %f R$'%(salario,int(pAumento),pAumento/100*salario,salarioF))
