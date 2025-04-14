import urllib.request as request
import json
from time import sleep

URL_SERVICO = "http://localhost:5000"
URL_ALIVE = f"{URL_SERVICO}/alive"
URL_JOGATINA = f"{URL_SERVICO}/jogatina"
URL_SISTEMAS = f"{URL_SERVICO}/sistemas"


def acessar(url):
	sucesso, conteudo = False, None
	try:
		resposta = request.urlopen(url)
		conteudo = resposta.read().decode("utf-8")
		sucesso = True
	except Exception as e:
		print(f"Ocorreu um erro acessando a URL: {url}")

	return sucesso, conteudo

def is_alive():
	sucesso, alive = acessar(URL_ALIVE)
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
		if is_alive():

			sucesso, noticias = get_jogatina()
			imprimir("Jogos Eletrônicos", noticias, sucesso)

			sucesso, noticias = get_sistemas()
			imprimir("Sistemas Operacionais", noticias, sucesso)
		else:
			print(f"Serviço de notícias indisponível")

		sleep(3)


