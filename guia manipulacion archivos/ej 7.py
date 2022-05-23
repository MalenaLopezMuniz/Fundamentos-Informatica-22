# 7. escribí un porgrama que lea un archivo e identifique la palabra más larga, 
# la cual debe imprimir y decir cuantos caracteres tiene.

def main():
    origen = "txt.txt"
    clean_arch = []
    contador = 0
    bandera = True
    
    archorigen = open(origen,'r')
    lst_arch = archorigen.readlines()
    
    for x in lst_arch:
        if x[len(x)-1] == '\n':    #<------- pregunta si hay \n
            x = x[:-1]             #<------- saca el \n
        clean_arch.append(x) #<------- archivo en lst limpio
    
    for x in clean_arch:     #<------- buscamos la palabra mas larga en el archivo limpio
        palabra = x
        print(x)
        if bandera:
            palabra_maxima = palabra
            bandera = False
        if len(palabra) >= len(palabra_maxima):
            palabra_maxima = palabra
            
    archorigen.close() 
    print(palabra_maxima) 
main()