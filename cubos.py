print ("ESTE PROGRAMA GENERA UN INTERVALO DE LOS CUBOS DE N NUMEROS")
n = int(raw_input('Introduce un numero entero: '))
a = range(1, n)
for x in range(0,n-1):
    a[x] = a[x] ** 3
print a