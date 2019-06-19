def mesE():
	data=str(input('Data (formato dd/mm/aaaa): '))
	mes=int(data[3:5])
	i=0
	mesE=['janeiro','fervereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
	while i<=len(mesE):
		if (mes-1)==i:
			print('%s de %s de %s'%(data[:2],mesE[i],data[6:]))
		i=i+1
