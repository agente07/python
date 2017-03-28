print ("ESTE PROGRAMA PERMITE OBTENER LA MEDIA DE 3 NUMEROS")
def mediadetresnumeros (x,y,z):
	media = (x+y+z)/3
	return (media)

num1=float(raw_input("introduce el primer numero: "))
num2=float(raw_input("introduce el segundo numero: "))
num3=float(raw_input("introduce el tercer numero: "))
print("la media es: ")
print mediadetresnumeros(num1,num2,num3)