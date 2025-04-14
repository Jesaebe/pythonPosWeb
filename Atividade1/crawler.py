import requests
import json
from time import sleep

PRODUCTS = "/home/jesaweb/Documents/pythonPosWeb/Atividade1/datas/products.json"
ORDERS = "/home/jesaweb/Documents/pythonPosWeb/Atividade1/datas/orders.json"
CART = "/home/jesaweb/Documents/pythonPosWeb/Atividade1/datas/cart.json"

URL_SERVICE_PRODUCTS = "http://localhost:5001/send"
URL_SERVICE_ORDERS = "http://localhost:5002/send"
URL_SERVICE_CART = "http://localhost:5003/send"


def send(url, get_file, data):
  success = False

  with open(get_file, "r") as file:
    content = json.load(file)
    json_data = content[data]    
    file.close()

    response = requests.post(url, json=json.dumps(json_data))
    success = response.status_code == 201

  return success

if __name__ == "__main__":
  while True:
    success = send(URL_SERVICE_PRODUCTS, PRODUCTS, "products")
    if success:
      print(f"Success sent foods")
    else:
      print(f"Some wrong happenned, can not send foods")
    print()

    success = send(URL_SERVICE_ORDERS, ORDERS, "orders")
    if success:
      print(f"Success sent orders")
    else:
      print(f"Some wrong happenned, can not send orders")
    print()

    success = send(URL_SERVICE_CART, CART, "cart")
    if success:
      print(f"Success sent cart")
    else:
      print(f"Some wrong happenned, can not send cart")
    print()
    
    
    sleep(5)