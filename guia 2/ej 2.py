# 2. Escribí un programa que pida un número y diga si es positivo, negativo o 0 
#y además informe si es par o impar (el 0 es un número par).
def signo (numero) :
    if numero > 0 :
        print ("es positivo")
    else:
        if numero == 0:
            print ("es cero")
        else:
            print ("es negativo")
def paridad (numero) :
    if numero % 2 == 0:
        print ("es par")
    else: 
        print ("es impar")
    
def main ():
    numero = int(input(" ingrese un numero: "))
    signo(numero)
    paridad(numero)

main() 