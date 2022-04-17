# 9. En este ejercicio hay que determinar cuánto tiempo tomaría ahorrar la cantidad suficiente de dinero para pagar el depósito. Para esto vamos a tomar algunas suposiciones:

# Llamemos al valor de la casa costo_total.
# El porcentaje de este costo que se corresponde con el depósito será porcentaje_deposito. # 25%.
# La cantidad actual de ahorros, cantidad_ahorrada, empezará en 0.
# Consideremos que se realiza una inversión del dinero ahorrado por la cual se obtiene cierta ganancia, g, por año 
# (es decir, por mes se obtendrían cantidad_ahorrada multiplicada por g/12). # 4% (g = 0.04).
# El sueldo anual será sueldo_anual.
# La cantidad que se ahorra por mes será porcentaje_ahorrado, el cual debe ser expresada como un valor decimal del sueldo mensual (si es 10%, este porcentaje será 0.1)
# Por último, al sueldo mensual lo llamaremos sueldo_mensual (sueldo_anual/12)
# El programa debe calcular cuantos meses tomaría ahorrar el dinero necesario para pagar el depósito. Este programa debe preguntarle al usuario cual es su sueldo anual, que porcentaje del sueldo quiere ahorrar por mes y cual es el costo de la casa en cuestión.


costo_total = int(input("Valor casa : $")) 
sueldo_anual = int(input("Sueldo anual : $")) 
porcentaje_ahorrado = float(input("Porcentaje de sueldo ahorrado por mes : ")) 
porcentaje_deposito = 0.25 
g = 0.04 

valor_deposito = costo_total*porcentaje_deposito 
print(valor_deposito)

sueldo_mensual = sueldo_anual/12 
print(sueldo_mensual)

ahorro_mensual = sueldo_mensual*porcentaje_ahorrado 
print(ahorro_mensual)

ganancia_mensual = ahorro_mensual+(g/12)
print(ganancia_mensual)

i=1
cantidad_ahorrada = 0 

while cantidad_ahorrada<valor_deposito:
    cantidad_ahorrada+= ganancia_mensual
    i+=1
print("La cantidad de meses es: {0}".format(i))

