#Calculadora de precios
iva = 0.19
producto = eval(input("ingrese el valor unitario del producto:"))
cantidad = eval(input("ingrese la cantidad de productos:"))
subtotal = producto * cantidad
aux = str(input('Ingrese s o n:'))

if aux == 's':
    print('IVA INCLUÍDO')
else: print('PRODUCTO SIN IVA')

print('SUBTOTAL: subtotal')
