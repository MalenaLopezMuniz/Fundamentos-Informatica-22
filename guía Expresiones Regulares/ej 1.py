# 1. Escribí un programa que verifique si un string tiene al menos un carácter permitido. 
#Estos caracteres son a-z, A-Z y 0-9.

import re 
texto = str(input("escriba texto: "))
caracteres = "[a-zA-Z0-9]"
def verificar (caracteres,texto):
    if not re.search(caracteres, texto):
        print("no verificado")
    else:
        print("verificado")
print(verificar(caracteres,texto))