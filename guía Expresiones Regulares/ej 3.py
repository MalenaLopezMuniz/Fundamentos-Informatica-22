# 3. Creá un programa que verifique las siguientes condiciones:
# si un string dado tiene una h seguida de ninguna o más e.
# si un string dado tiene una h seguida de una o más e.
# si un string dado tiene una h seguida de dos o tres e.


import re

def encontrar_patron(string):
    patron = "he*"
    if re.search(patron,string):
        return("verificado")
    else:
        return("no verificado")

def encontrar_patron(string):
    patron = "he+"
    if re.search(patron,string):
        return("verificado")
    else:
        return("no verificado")

def encontrar_patron(string):
    patron = "he{2,3}"
    if re.search(patron,string):
        return("verificado")
    else:
        return("no verificado")


print(encontrar_patron("a"))
print(encontrar_patron("hee"))