from flask import Flask, Response, request
from kafka import KafkaClient, KafkaProducer
from kafka.errors import KafkaError
from time import sleep
import secrets, json

PROCESSO = "ebook"

URL_KAFKA = "kafka:29092"
KAFKA_CLIENT = KafkaClient(bootstrap_servers = [URL_KAFKA], api_version=(0, 10, 1))
KAFKA_PRODUCER = KafkaProducer(bootstrap_servers = [URL_KAFKA], api_version=(0, 10, 1))
STATUS = {
  "OK": 200,
  "NO_CONTENT": 204,
  "UNPROCESSABLE_CONTENT": 422
}

servico = Flask(PROCESSO)

INFO = {
  "descricao" : "Serviços para venda de ebooks",
  "versao" : "0.0.1"
}

def iniciar():
  iniciado = False
  try:
    cliente = KAFKA_CLIENT
    cliente.add_topic(PROCESSO)
    cliente.close()

    iniciado = True
  except Exception as e:
    print(f"Error ao iniciar o Kafka: {str(e)}")

  return iniciado

@servico.get("/")
def get_info():
  return Response(json.dumps(INFO), status=STATUS["OK"])

@servico.post("/vender")
def vender():
  sucesso, id, dados = False, secrets.token_hex(16), request.json
  #Aqui teria a lógica de validação de dados e inicio do processamento da venda
  sleep(2)

  try:
    venda = {
      "id": id,
      "sucesso": 1,
      "mensagem": "venda de ebook iniciada",
      "id_cliente": dados["id_cliente"],
      "id_ebook": dados["id_ebook"],
      "quantidade": dados["quantidade"]
    }

    produtor = KAFKA_PRODUCER
    produtor.send(topic=PROCESSO, value=json.dumps(venda).encode("utf-8"))
    produtor.flush()

    sucesso = True
  except Exception as e:
    print(f"Error ao realizar venda de ebooks: {str(e)}")

  return Response(status=STATUS["NO_CONTENT"] if sucesso else STATUS["UNPROCESSABLE_CONTENT"])

if __name__ == "__main__":
  iniciado = iniciar()
  if iniciado:
    servico.run(host="0.0.0.0", debug=True)
  else:
    print("Error ao iniciar vendas de ebooks")
