def media():
	i=0
	alunosM=[]
	while i<10:
		x=1
		media=0
		while x<=4:
			nota=float(input('Nota %d: '%(x)))
			media=media+(nota/4)
			x=x+1
		alunosM=alunosM+[media]
		i=i+1
	y=0
	z=0
	while y<10:
		if alunosM[y]>=7:
			z=z+1
		y=y+1
	return z
