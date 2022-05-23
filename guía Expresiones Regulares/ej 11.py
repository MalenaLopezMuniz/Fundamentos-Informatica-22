#Realizá un programa que dado una lista de strings verifique que dos palabras dentro del 
# string empiecen con la letra P y las imprima.
#  (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).

import re

def encontrar_palabras(lista):
    patron = "(P\w*)\W(P\w*)"
    for elemento in lista:
        # resultado = re.match(patron,lista)
        # if resultado is not None:
            print(re.match(patron,elemento))
            #print(resultado)
lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]

def encontrar_palabras(lista):
    patron = "(P\w*)\W(P\w*)"
    for elemento in lista:
        resultado = re.match(patron,lista), elemento
        if resultado is not None:
            print(resultado.group())
lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
encontrar_palabras(lista)



