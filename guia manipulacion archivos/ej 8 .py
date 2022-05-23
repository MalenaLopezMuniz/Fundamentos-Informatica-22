# 8. Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.


def main():
    arch=open("Origen1.txt","r") 
    arch1= arch.readlines()   
    arch.close() 

    arch=open("Origen2.txt","r") 
    arch2= arch.readlines()    
    arch.close() 

    arch=open("Destino.txt","r")  
    arch3= arch.readlines()    
    arch.close() 

    lst=[]
    for x in arch1:
        lst.append(x)
    for x in arch2:
        lst.append(x)
    for x in arch3:
        lst.append(x)
    
    arch4=open("Destino.txt","w")  
    arch4.write(lst)    
    arch4.close()


main()

