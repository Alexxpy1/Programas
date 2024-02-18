"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
valor = (input('Ingrese el precio del producto en formato #.##: '))
euro = valor[:valor.find('.')]
centimos = valor[valor.find('.') + 1:] 
print(f'Son {euro} euros con {centimos} céntimos')