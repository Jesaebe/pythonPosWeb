from flask import Flask, Response, request
from pymemcache.client import base
import json

VERSAO = "1.0"
INFO = {
	"descricao": "Serviço que disponibilizar notícias sobre Jogos Eletrônicos",
	"autor": "Jesaebe Prado",
	"versao": VERSAO
}

ALIVE = "SIM"

BANCO_NOTICIAS = "banco_jogatina"
PORTA_BANCO = "11211"

servico = Flask("noticias")

@servico.get("/")
def getinfo():
	return Response(json.dumps(INFO), status=200, mimetype="application/json")

@servico.get("/info")
def get_info():
	return Response(json.dumps(INFO), status=200, mimetype="application/json")

@servico.get("/alive")
def is_alive():
	return Response(ALIVE, status=200, mimetype="text/plan")

@servico.post("/gravar")
def gravar_jogatina():
  sucesso, noticias = False, request.get_json()
  try:
    cliente = base.Client((BANCO_NOTICIAS, PORTA_BANCO))
    cliente.set("jogatina", noticias)
    cliente.close()
    sucesso = True
  except Exception as e:
    print(f"Ocorreu um erro ao gravar notícias: {str(e)}")
	
  return Response(status=201 if sucesso else 422)

@servico.get("/noticias")
def get_jogatina():  
  sucesso, noticias = False, []
  try:
    cliente = base.Client((BANCO_NOTICIAS, PORTA_BANCO))
    noticias = cliente.get("jogatina")    
    cliente.close()
    sucesso = True
  except Exception as e:
    print(f"Ocorreu um erro acessando notícias: {str(e)}")

  return Response("{}" if noticias is None else noticias, status=200 if sucesso else 204, mimetype="application/json")

if __name__ == "__main__":
	servico.run(host="0.0.0.0", debug=True)