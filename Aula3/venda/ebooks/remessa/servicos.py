from flask_apscheduler import APScheduler
from time import sleep
from kafka import KafkaClient, KafkaConsumer, KafkaProducer, TopicPartition
import random, json

PROCESSO = "estoque"
PROCESSO_ANTERIOR = "ebook"

URL_KAFKA = "kafka:29092"
KAFKA_CONSUMER = KafkaConsumer(
  bootstrap_servers = [URL_KAFKA], 
  api_version=(0, 10, 1),
  auto_offset_reset = "earliest",
  consumer_timeout_ms = 1000
)
KAFKA_CLIENT = KafkaClient(bootstrap_servers = [URL_KAFKA], api_version=(0, 10, 1))
KAFKA_PRODUCER = KafkaProducer(bootstrap_servers = [URL_KAFKA], api_version=(0, 10, 1))

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

def validar_dados(dados):
  ...
  
offset = 0
def executar():
  consumidor = KAFKA_CONSUMER
  topico = TopicPartition(PROCESSO_ANTERIOR, 0)
  consumidor.assign([topico])
  consumidor.seek(topico, offset)

  produtor = KAFKA_PRODUCER 

  for dados in consumidor:
    offset = dados.offset + 1
    validos, mensagem = validar_dados(dados)
    sleep(2)
    if validos: 
      #Simulando um processamento de estoque
      dados["sucesso"] = 1
    else:
      dados["sucesso"] = 0
    dados["mensagem"] = mensagem

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