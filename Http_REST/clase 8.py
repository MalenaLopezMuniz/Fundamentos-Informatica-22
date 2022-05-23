import requests

#Obtengo todos los objetos (prendas)
pedido = requests.get("https://macowins-server.herokuapp.com/prendas")
print(pedido.json()) 

#1 
pedido = requests.get("https://macowins-server.herokuapp.com/prendas/20")
print(pedido.json())

#2
pedido = requests.get("https://macowins-server.herokuapp.com/prendas/400")
print(pedido.json())

# Para saber cuántas prendas hay hago:
pedido = requests.get("https://macowins-server.herokuapp.com/prendas")
print(len(pedido.json()))

#3
pedido = requests.get("https://macowins-server.herokuapp.com/prendas/20")
print(pedido.json())


pedido = requests.get("https://macowins-server.herokuapp.com/prendas/400")
print(pedido) #devuelve Error404
print(pedido.headers) #me trae la metadata relacionada al pedido.
#pedido es un objeto, headers es un atributo.

pedido = requests.get("https://macowins-server.herokuapp.com/prendas/20")
# pedido = requests.get("https://macowins-server.herokuapp.com/prendas")
print(pedido.status_code) #status code, es un atributo del objeto


