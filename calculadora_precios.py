#Calculadora de precios
iva = 1.19
producto = eval(input("ingrese el valor unitario del producto:"))
aux = str(input('¿El producto está gravado con IVA? Ingrese S o N:'))
cantidad = eval(input("ingrese la cantidad de productos:"))
subtotal = producto * cantidad

if aux == 'S':
    print('IVA INCLUÍDO')
else: print('PRODUCTO SIN IVA')

if aux == 'S':
    subtotal *= iva

print(f'SUBTOTAL: {subtotal}')

aux2 = str(input('¿Faltan productos por cobrar? Ingrese S o N:'))

while aux2 == 'S':
    producto = eval(input("ingrese el valor unitario del producto:"))
    aux = str(input('¿El producto está gravado con IVA? Ingrese S o N:'))
    cantidad = eval(input("ingrese la cantidad de productos:"))
    subtotal = producto * cantidad

    if aux == 'S':
        print('IVA INCLUÍDO')
    else: print('PRODUCTO SIN IVA')

    if aux == 'S':
        subtotal *= iva

    print(f'SUBTOTAL: {subtotal}')

    aux2 = str(input('¿Faltan productos por cobrar? Ingrese S o N:'))

    if aux2 == 'N':
        break

print(f'TOTAL A COBRAR: {subtotal}')
