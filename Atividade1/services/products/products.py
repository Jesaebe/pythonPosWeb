from flask import Flask, Response, request
from flask_cors import CORS
from pymemcache.client import base
import json

VERSAO = '1.0.0'

INFO = {
  'description': 'Service that list fastfoods',
  'actor': 'Jesaebe (JesaWeb) Prado',
  'version': VERSAO
}

ALIVE = 'YES'

DB_FOOD = "db_foods"
DB_PORT = "11211"

service = Flask("products")
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
def send_foods():
  success, foods = False, request.get_json()  
  try:
    client = base.Client((DB_FOOD, DB_PORT))
    client.set("products", foods)
    client.close()
    success = True
  except Exception as e:
    print(f"Some wrong happenned, can not send data: {str(e)}")
	
  return Response(status=201 if success else 422)

@service.get("/foods")
def get_foods():
  success, foods = False, []
  try:
    client = base.Client((DB_FOOD, DB_PORT))
    foods = client.get("products")    
    client.close()
    success = True
  except Exception as e:
    print(f"Some wrong happenned, can not get data: {str(e)}")

  return Response("{}" if foods is None else foods, status=200 if success else 204, mimetype="application/json")

if __name__ == "__main__":
	service.run(host="0.0.0.0", debug=True)