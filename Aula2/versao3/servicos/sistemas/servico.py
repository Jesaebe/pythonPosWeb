from flask import Flask, Response
import json

VERSAO = "1.0"
INFO = {
	"descricao": "Serviço que disponibilizar notícias sobre Sistemas Operacionais",
	"autor": "Jesaebe Prado",
	"versao": VERSAO
}

SISTEMAS = [
    {
        "id": 1,
        "data": "22/05/2019",
        "titulo": "Estes são os 12 problemas já encontrados na atualização do Windows 10",
        "endereco": "https://olhardigital.com.br/noticia/microsoft-lista-todos-os-problemas-da-nova-atualizacao-do-windows-10/86052",
    },
    {
        "id": 2,
        "data": "10/05/2015",
        "titulo": "Atualização do Windows 10 está causando problemas para alguns usuários",
        "endereco": "https://canaltech.com.br/windows/atualizacao-do-windows-10-esta-causando-problemas-para-alguns-usuarios-46921/",
    },
    {
        "id": 3,
        "data": "04/05/2016",
        "titulo": "Top 5 distribuições Linux que podem substituir o Windows 10",
        "endereco": "https://pplware.sapo.pt/linux/top-5-distribuies-gnulinux-que-podem-substituir-o-windows-10/",
    }
]

ALIVE = "SIM"

servico = Flask("noticias")

@servico.get("/")
def getinfo():
	return Response(json.dumps(INFO), status=200, mimetype="application/json")

@servico.get("/info")
def get_info():
	return Response(json.dumps(INFO), status=200, mimetype="application/json")

@servico.get("/alive")
def is_alive():
	return Response(ALIVE, status=200, mimetype="text/plan")

@servico.get("/noticias")
def get_sistemas():
	return Response(json.dumps(SISTEMAS), status=200, mimetype="application/json")

if __name__ == "__main__":
	servico.run(host="0.0.0.0", debug=True)