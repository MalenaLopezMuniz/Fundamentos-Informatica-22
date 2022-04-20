# 3.Escribí un programa que lea un archivo, guarde las líneas del archivo
# en una lista y luego imprima las n últimas.

def main():
    lst = []
    lineas = int(input("Ingrese la cantidad de lineas: "))

    arch=open("txt.txt","r")  
    ver= arch.readlines()    
   

    for x in range(0,len(ver)):
        palabra = ver[x]         
        palabra = palabra[:-1]   
        lst.append(palabra)     
    
    for x in range(len(lst)-lineas,len(lst)):
        print(lst[lineas:])

    arch.close() 
main()

#supe hacer que encuentre las primeras ultimas lineas en base a eliminar las primeras n (que ingresa en el input) no se como hacer para que encuentre las ultimas n