from flask import Flask, Response, request
import requests
import json

servico = Flask("servicos")

ROTA_EBOOK = "http://ebook:5000/vender"
ROTA_GIFTCARD = "http://giftcard:5000"

INFO = {
  "descricao": "Serviço de vendas de ebooks e giftcards",
  "versao": "0.0.1"
}

@servico.get("/")
def get_info():
  return Response(json.dumps(INFO), status=200, mimetype="application/json")

@servico.post("/ebook")
def vender_ebook():
    resposta = requests.post(ROTA_EBOOK, json=request.json)
    return Response(status=resposta.status_code)

@servico.post("/giftcard")
def vender_giftcard():
   resposta = requests.post(f'{ROTA_GIFTCARD}/vender', json=request.json)
   return Response(status=resposta.status_code)


if __name__ == "__main__":
  servico.run(host="0.0.0.0", debug=True)
