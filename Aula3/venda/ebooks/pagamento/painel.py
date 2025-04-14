from kafka import KafkaConsumer, TopicPartition
from time import sleep
import json

URL_KAFKA = "kafka:29092"
KAFKA_CONSUMER = KafkaConsumer(
  bootstrap_servers = [URL_KAFKA], 
  api_version=(0, 10, 1),
  auto_offset_reset = "earliest",
  consumer_timeout_ms = 1000
)

if __name__ == "__main__":
  print("Esperando vendas...")
  painel = KAFKA_CONSUMER
  topico = TopicPartition("pagamento", 0)
  painel.assign([topico])
  painel.seek_to_beginning(topico)

  while True:
    for venda in painel:
      dados = json.loads(venda.value)
      print(f"Dados da venda: {dados}")
  