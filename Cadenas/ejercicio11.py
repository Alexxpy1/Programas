"""
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""
nombreProducto = input('Ingrese el nombre del producto: ')
precio = float(input('Ingrese el precio del producto: '))
cantidad = int(input('Ingrese la cantidad adquirida: '))
costeTotal = precio * cantidad
print(f'{nombreProducto} tiene un precio de {precio:,.2f}, se compro {round(cantidad)} unidades y el coste total es {costeTotal:,.2f}')