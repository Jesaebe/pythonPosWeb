from flask_apscheduler import APScheduler
from time import sleep
from kafka import KafkaClient, KafkaConsumer, KafkaProducer, TopicPartition
import random, json

PROCESSO = "estoque"
PROCESSO_ANTERIOR = "ebook"

URL_KAFKA = "kafka:29092"
KAFKA_CONSUMER = KafkaConsumer(
  bootstrap_servers = [URL_KAFKA], 
  api_version = (0, 10, 1),
  consumer_timeout_ms = 1000,
  auto_offset_reset = "earliest",
  group_id = PROCESSO
)
KAFKA_CLIENT = KafkaClient(bootstrap_servers = [URL_KAFKA], api_version=(0, 10, 1))
KAFKA_PRODUCER = KafkaProducer(bootstrap_servers = [URL_KAFKA], api_version=(0, 10, 1))

def iniciar():
  global offset
  offset = 0

  iniciado = False
  try:
    cliente = KAFKA_CLIENT
    cliente.add_topic(PROCESSO)
    cliente.close()

    iniciado = True
  except Exception as e:
    print(f"Error ao iniciar o Kafka: {str(e)}")

  return iniciado

def validar_dados(dados):
  validos, titulo, mensagem, total = (dados["sucesso"] == 1), "", "", 0.0
  titulo = "Implementando SOA usando JAVATM EE"
  sleep(2) #Simula um processamento do estoque
  if validos:
    mensagem = "Quantidade do Ebook separada com sucesso"
  else:
    mensagem = "Erro serapado quantidade do Ebook"

  total = dados["quantidade"] * 20.0

  return validos, titulo, mensagem, total  

def executar():
  global offset
  consumidor = KAFKA_CONSUMER
  topico = TopicPartition(PROCESSO_ANTERIOR, 0)
  consumidor.assign([topico])
  consumidor.seek(topico, offset) 

  produtor = KafkaConsumer(bootstrap_servers = [URL_KAFKA], api_version = (0, 10, 1),consumer_timeout_ms = 1000,auto_offset_reset = "earliest",group_id = PROCESSO)
  
  for dados in consumidor:

    offset = dados.offset + 1
    dados = json.loads(dados.value)
    validos, titulo, mensagem, total = validar_dados(dados)
    
    if validos: 
      #Simulando um processamento de estoque
      dados["sucesso"] = 1
    else:
      dados["sucesso"] = 0

    dados["mensagem"] = mensagem
    dados["titulo"] = titulo
    dados["total"] = total

    print(dados)
    
    produtor.send(PROCESSO, json.dumps(dados).encode("utf-8"))  

  produtor.flush()
  produtor.close()

  consumidor.close()
    
if __name__ == "__main__":  
  if iniciar():
    servico = APScheduler()
    servico.add_job(id=PROCESSO, func=executar, trigger="interval", seconds=3)
    servico.start()

    while True:
      sleep(60)