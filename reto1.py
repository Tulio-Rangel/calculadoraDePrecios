i = 1
val2=0
subt=0

while i > 0 : 
	val = float(input("Ingrese el valor unitario: "))
	iva = input("¿El producto cuenta con IVA? ingrese S o N: ")
	cant = float(input("Ingrese la cantidad de producto/s que lleva el cliente: "))

	if iva =="S":
		val2 = val*1.19*cant 
		print("IVA incluído")
	elif iva =="N":
		val2 = val*cant
		print("PRODUCTO SIN IVA")
	else: 
		print("PRODUCTO SIN IVA")
		val2 = val*cant
	subt+=float(val2)
	print(f"SUBTOTAL: {subt}")
	add = input("¿Faltan productos por producos por cobrar? ingrese S o N: ")
	if add =="S":
		i =1
	else:
		i=0
print(f"TOTAL A COBRAR: {subt}")

