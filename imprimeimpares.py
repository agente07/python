
def funcion1(num):
	for num in range(13, 32):
		if num % 2 != 0:
			print (num)
	
	return num


num1=int(raw_input("Ingrese un numero = "))
print ("ESTE PROGRAMA SOLO IMPRIME LOS PRIMEROS 10 NUMEROS IMPARES A PARTIR DEL 13")

print funcion1(num1)



#for num in range(13, 32):
#	if num % 2 != 0:
#		print (num)