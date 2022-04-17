#11. Modificá el programa anterior para que además imprima los caracteres que no aparecen en la cadena, 
# pero con el valor 0.
contadores = {}
alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
for letra in alfabeto:
	contadores[letra]=0

cadena = input("escribi una palabra:")
for caracter in cadena:
	if caracter in alfabeto:
		contadores[caracter]+=1

for valor in contadores.keys():
    print(valor,contadores[valor])