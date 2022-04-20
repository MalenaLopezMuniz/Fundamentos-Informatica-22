# 2. Escribí un programa que lea un archivo e imprima las primeras n líneas.

def main():  
    lst = []
    n = int(input("ingrese cant lineas: "))
    arch = open("txt.txt","r")  
    ver = arch.readlines()   

    for x in range(0,len(ver)):
        palabra = ver[x]         
        lst.append(palabra)      
    
    for x in range(0,n):
        print(lst[x])

    arch.close() 
main()

        