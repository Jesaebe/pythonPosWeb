from kafka import KafkaConsumer, TopicPartition
from time import sleep
import json

def atender_pacientes():
  consumidor = KafkaConsumer(
    bootstrap_servers = ["0.0.0.0:9092"],
    api_version = (0, 10, 1),
    auto_offset_reset = "earliest",
    consumer_timeout_ms = 1000
  )

  topico = TopicPartition("pacientes", 0)
  consumidor.assign([topico])

  contador = 0
  while True:
    for atendimento in consumidor:
      if atendimento:
        paciente = json.loads(atendimento.value)
        print(f"paciente {paciente['nome']} sendo atendido(a) pelo {paciente['especialidade']}")
        contador += 1
    print(f"Foram atendidos {contador} pacientes")
    sleep(3)

if __name__ == "__main__":
  atender_pacientes()
