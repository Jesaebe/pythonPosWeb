from kafka import KafkaClient, KafkaProducer
from faker import Faker
import random
import json

ESPECIALIDADES = ["Ortopedista", "Cardiologista", "Endocrinologista","Urologista","Pneumologista"]
TOTAL_PACIENTES = 20

def iniciar_fila_atendimento():
  iniciada = False
  try:
    cliente = KafkaClient(
      bootstrap_servers = ["0.0.0.0:9092"],
      api_version = (0, 10, 1)
    )
    cliente.add_topic("Pacientes")
    cliente.close()
    iniciada = True
  except Exception as e:
    print(f"Erro ao iniciar fila de atendimento: {str(e)}")

  return iniciada

def gerar_paciente_fake():
  fake = Faker("pt_BR")
  nome = fake.name()
  endereco = fake.address()
  idade = random.randint(14,100)
  especialidade = random.choice(ESPECIALIDADES)
  print(f"Nome do Paciente: {nome}, idade: {idade}")
  print(f"Endereço do Paciente: {endereco}")
  print(f"Especialidade: {especialidade}")

  return {
    "nome": nome,
    "idade": idade,
    "endereco": endereco,
    "especialidade": especialidade
  }

def on_success(mensagem_de_sucesso):
  print(f"Sucesso, enviando paciente: {mensagem_de_sucesso}")

def on_erro(mensagem_de_erro):
  print(f"Error ao enviar paciente: {mensagem_de_erro}")

def gerar_fila_atendimento(): 
  produtor = KafkaProducer(
    bootstrap_servers = ["0.0.0.0:9092"],
    api_version = (0, 10, 1)
  )

  for _ in range(TOTAL_PACIENTES):
    paciente = gerar_paciente_fake()
    print(f"Enviando o paciente {paciente['nome']} para a fila do {paciente['especialidade']}")

    envio = produtor.send(topic="pacientes", value=json.dumps(paciente).encode("utf-8"))
    envio.add_callback(on_success).add_errback(on_erro)

    produtor.flush()

  produtor.close()

if __name__ == "__main__":
  iniciada = iniciar_fila_atendimento()
  if iniciada:
    gerar_fila_atendimento()


