import requests


import requests

pedido = requests.get("https://macowins-server.herokuapp.com/prendas")

print (pedido)
#los servidores devuelven la informacion en este formato
print (pedido.json())
# como saber el total de las prendas
print (len(pedido.json()))
# si quiero ver si tiene 400 prendas 
print (requests.get("https://macowins-server.herokuapp.com/prendas/400"))
#header --> atributo -- trae la metadata del pedido 
print (pedido.headers)
#ststud code 
print(pedido.status_code)
