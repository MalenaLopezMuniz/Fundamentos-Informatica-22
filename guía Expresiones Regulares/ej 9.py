#Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
# (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")

import re

def entre_guiones(string):
    patron = r"-(.*?)-"
    return re.findall(patron, string)
string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
print(entre_guiones(string))