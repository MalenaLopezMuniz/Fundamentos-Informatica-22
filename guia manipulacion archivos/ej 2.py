# 2. Escribí un programa que lea un archivo e imprima las primeras n líneas.

def main():  
    lst = []
   
    arch = open("txt.txt","r")  
    ver = arch.readlines()   

    for x in range(0,len(ver)):
        palabra = ver[0,4]         
        lst.append(palabra)      
    
    for x in range(0,4):
        print(lst[x])

    arch.close() 
main()

        