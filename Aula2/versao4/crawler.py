import requests
import json
from time import sleep

NOTICIAS_JOGATINA = "/home/jesaweb/Documents/pythonPosWeb/Aula2/versao4/noticias/jogatina.json"
NOTICIAS_SISTEMAS = "/home/jesaweb/Documents/pythonPosWeb/Aula2/versao4/noticias/sistemas.json"

URL_SERVICO_JOGATINA = "http://localhost:5001/gravar"
URL_SERVICO_SISTEMAS = "http://localhost:5002/gravar"

def enviar(url, arquivo_noticias):
  sucesso = False

  with open(arquivo_noticias, "r") as arquivo:
    conteudo = json.load(arquivo)
    noticias = conteudo["noticias"]        
    arquivo.close()

    resposta = requests.post(url, json=json.dumps(noticias))
    
    sucesso = resposta.status_code == 201

  return sucesso

if __name__ == "__main__":
  while True:
    sucesso = enviar(URL_SERVICO_JOGATINA, NOTICIAS_JOGATINA)
    if sucesso:
      print(f"Notícias sobre Jogos Eletrônicos enviada")
    else:
      print(f"Erro ao enviar notícias sobre Jogos Eletrônicos")
    print()
    sucesso = enviar(URL_SERVICO_SISTEMAS, NOTICIAS_SISTEMAS)
    if sucesso:
      print(f"Notícias sobre Sistemas Operacionais enviada")
    else:
      print(f"Erro ao enviar notícias sobre Sistemas Operacionais")
    
    sleep(10)