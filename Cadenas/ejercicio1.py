"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""
usuario = input('Ingrese su nombre: ')
entero = int(input('Ingrese un número entero: '))
print(f"{usuario} \n" * entero)

