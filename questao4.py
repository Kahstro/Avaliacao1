def salario():
	ganhoH=float(input('Ganho por hora:'))
	horasM=int(input('Horas trabalhadas no mes:'))
	salarioB=ganhoH*horasM
	ir=(11/100)*salarioB
	inss=(8/100)*salarioB
	sindicato=(5/100)*salarioB
	salarioL=salarioB-(ir+inss+sindicato)
	return print('Salario bruto: %f R$\nINSS: %f R$\nSindicato: %f R$\nSalario liquido: %f R$'%(salarioB,inss,sindicato,salarioL))
