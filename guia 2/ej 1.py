# 1. Crea un programa que lea una cadena por teclado y compruebe si la primer letra es mayuscula o minuscula.


cadena = str(input("ingresar palabra:"))
def es_mayus(palabra):
     if palabra[0] >= "a" and palabra[0] <= "z":
         print("es minuscula")
     else:
         print("es mayuscula")
print(es_mayus(cadena))
