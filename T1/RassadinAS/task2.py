#!/usr/bin/python

i=0
flag=0
mas=[]
while (flag==0) :
	arr=raw_input("enter the string or '"'end'"'- ")
	if (arr=="end") :
		flag=1
	else :
		mas.append(map(float,arr.split()))
		maximum=1.0
		for j in range(len(mas[i])) :
			if (maximum<mas[i][j]) :
				maximum=mas[i][j]
		for j in range(len(mas[i])) :
			mas[i][j]/=maximum
		i+=1
		print "new itteration"
print mas

