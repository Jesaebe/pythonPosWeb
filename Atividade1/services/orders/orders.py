from flask import Flask, Response, request
from flask_cors import CORS
from pymemcache.client import base
import json

VERSAO = '1.0.0'

INFO = {
  'description': 'Service that list orders',
  'actor': 'Jesaebe (JesaWeb) Prado',
  'version': VERSAO
}

ALIVE = 'YES'

DB_ORDER = "db_orders"
DB_PORT = "11211"

service = Flask("orders")
CORS(service)

@service.get("/")
def getinfo():
	return Response(json.dumps(INFO), status=200, mimetype="application/json")

@service.get("/info")
def get_info():
	return Response(json.dumps(INFO), status=200, mimetype="application/json")

@service.get("/alive")
def is_alive():
	return Response(ALIVE, status=200, mimetype="text/plan")

@service.post("/send")
def send_orders():
  success, orders = False, request.get_json()  
  try:
    client = base.Client((DB_ORDER, DB_PORT))
    client.set("orders", orders)
    client.close()
    success = True
  except Exception as e:
    print(f"Some wrong happenned, can not send data: {str(e)}")
	
  return Response(status=201 if success else 422)

@service.get("/orders")
def get_orders():
  success, orders = False, []
  try:
    client = base.Client((DB_ORDER, DB_PORT))
    orders = client.get("orders")    
    client.close()
    success = True
  except Exception as e:
    print(f"Some wrong happenned, can not get data: {str(e)}")

  return Response("{}" if orders is None else orders, status=200 if success else 204, mimetype="application/json")

if __name__ == "__main__":
	service.run(host="0.0.0.0", debug=True)