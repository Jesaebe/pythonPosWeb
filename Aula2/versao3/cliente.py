import urllib.request as request
import json
from time import sleep

URL_SERVICO_JOGATINA = "http://localhost:5001"
URL_ALIVE_JOGATINA = f"{URL_SERVICO_JOGATINA}/alive"
URL_JOGATINA = f"{URL_SERVICO_JOGATINA}/noticias"

URL_SERVICO_SISTEMAS = "http://localhost:5002"
URL_ALIVE_SISTEMAS = f"{URL_SERVICO_SISTEMAS}/alive"
URL_SISTEMAS = f"{URL_SERVICO_SISTEMAS}/noticias"



def acessar(url):
	sucesso, conteudo = False, None
	try:
		resposta = request.urlopen(url)
		if resposta.code == 200:
			conteudo = resposta.read().decode("utf-8")
			sucesso = True
	except Exception as e:
		print(f"Ocorreu um erro acessando a URL: {url}")

	return sucesso, conteudo

def is_alive_jogatina():
	sucesso, alive = acessar(URL_ALIVE_JOGATINA)
	return sucesso and alive == "SIM"

def is_alive_sistemas():
	sucesso, alive = acessar(URL_ALIVE_SISTEMAS)
	return sucesso and alive == "SIM"

def get_jogatina():
	sucesso, noticias = acessar(URL_JOGATINA)
	if sucesso:
		noticias = json.loads(noticias)
	return sucesso, noticias

def get_sistemas():
	sucesso, noticias = acessar(URL_SISTEMAS)
	if sucesso: 
		noticias = json.loads(noticias)
	return sucesso, noticias

def imprimir(tipo_noticia, noticias, sucesso):
	if sucesso:
		print(f"Últimas notícias sobre {tipo_noticia}")
		for contador, noticia in enumerate(noticias):
			print(f"#{contador + 1}: {noticia}")
	else: 
		print(f"Não foi possível obter {tipo_noticia}")
			
if __name__ == "__main__":
	while True:
		if is_alive_jogatina():
			sucesso, noticias = get_jogatina()
			imprimir("Jogos Eletrônicos", noticias, sucesso)
		else:
			print(f"Serviço de notícias de Jogos Eletrônicos indisponível")

		print()		

		if is_alive_sistemas():
			sucesso, noticias = get_sistemas()
			imprimir("Sistemas Operacionais", noticias, sucesso)
		else:
			print(f"Serviço de notícias de Sistemas Operacionais indisponível")

		print()
		sleep(1)
		for i in range(0,3):
			print(f"Aguarde... {3 - i}")
			sleep(1)
		print()
		


