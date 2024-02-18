"""
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
"""
correoUsuario = input('Ingrese su correo: ')
usuario = correoUsuario[:correoUsuario.index('4')]
print(usuario + '@ceu.es')