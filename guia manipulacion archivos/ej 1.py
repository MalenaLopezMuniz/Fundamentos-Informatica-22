#1 . Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra

def main():
    ver = []
    arch = open("txt.txt","r") 
    ver = arch.readlines()  
    letra = input("ingrese una letra: ") 

    cont = 0

    for x in range(0,len(ver)):
        if(letra != ver[x][0]):
            cont+=1

    print(cont)
    arch.close() 
main()

# comentario para el profesor: supe como hacer que encuentre cuantas lineas empiezan con una letra, pero no cuantas NO empiezan.