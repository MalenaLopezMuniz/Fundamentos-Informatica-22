# 13. Creá un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo
#del otro creando la función esMultiplo

def esMultiplo (num1, num2):
    if num1 % num2 == 0:
            print ("{} es multiplo de {}".format(num1,num2))
    else:
            print ("{} no es multiplo de {}".format(num1,num2))
    if num2 % num1 == 0:
            print ("{} es multiplo de {}".format(num2,num1))
    else:
            print ("{} no es multiplo de {}".format(num2,num1))
def main():
    num1 = int(input("ingresar numero entero: "))
    num2 = int(input("ingresar numero entero: "))
    esMultiplo(num1,num2)
main()




