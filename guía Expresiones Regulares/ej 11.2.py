import re
lista = ["Práctica Python", "Práctica C++", "Práctica Fortran", "Pasdfghjk Pfghb"]
def empiezanP(lista):
    patron = "(P\w*)\W(P\w*)"
    for elemento in lista:
        resultado = re.match(patron, elemento)
        if resultado is not None:
            print(resultado.group())

empiezanP(lista)

def encontrar_palabras(lista):
    patron = "(P\w*)\W(P\w*)"
    for elemento in lista:
        resultado = re.match(patron,lista) , elemento
        if resultado is not None:
            print(resultado.group())
lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
empiezanP(lista)
