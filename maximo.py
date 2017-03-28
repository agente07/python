print ("ESTE PROGRAMA PERMITE OBTENER EL MAXIMO DE 3 NUMEROS")
def maximodetresnumeros(a,b,c):
	if a > b and a > c:
		print "el mayor es = " ,a
	if b > a and b > c:
		print "el mayor es = " ,b
	if c > a and c > b:
		print "el mayor es = " ,c

a=int(raw_input("introduce el primer numero: "))
b=int(raw_input("introduce el segundo numero: "))
c=int(raw_input("introduce el tercer numero: "))
print maximodetresnumeros(a,b,c)
