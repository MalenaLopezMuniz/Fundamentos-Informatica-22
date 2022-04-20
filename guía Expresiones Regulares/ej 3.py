# 3. Creá un programa que verifique las siguientes condiciones:
# si un string dado tiene una h seguida de ninguna o más e.
# si un string dado tiene una h seguida de una o más e.
# si un string dado tiene una h seguida de una o más e.
# si un string dado tiene una h seguida de dos o tres e.


import re 
texto = str(input("escriba texto: "))
caracteres = "h(e*)"
def verificar (caracteres,texto):
    if texto.match(caracteres):
        print("verificado")
    else:
        print("no verificado")
print(verificar(caracteres,texto))