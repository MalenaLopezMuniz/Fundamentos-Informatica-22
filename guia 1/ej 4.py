# 4. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayúsculas
NombreApellidos = input('Ingrese nombre y dos apellidos: ')
datos = NombreApellidos.split()
for palabra in datos:
    palabra = palabra.capitalize()
    print(palabra,end=' ')
print()

