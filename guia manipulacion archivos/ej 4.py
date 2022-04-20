# 4. Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y 
#luego imprima el resultado"

def main():

    arch=open("txt.txt","r")  
    ver= arch.readlines()    
    cond = True
    i=0
    pal=0
    lineas = 0

    while(cond):
        while(ver[i]=="\n"): 
            pal+=1
            cond = True

        pal+=1

        if ver[i]=='\n' and lineas == len(ver):
            cond = False

    print(pal)
        
    arch.close() 

main()