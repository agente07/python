print ("ESTE PROGRAMA PERMITE OBTENER EL VOLUMEN DE UNA ESFERA")
def volumen (rad):
	radio = (4* 3.1416 * rad**3) / 3
	return (radio)

rad = float(input("ingrese la radio de la espera: "))
print ("el volume es: ")
print volumen(rad)
