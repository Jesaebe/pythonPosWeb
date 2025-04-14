from flask import Flask

servico = Flask(__name__)

@servico.get("/info")
def get_info():
	return {
	"descricao": "cadastro simples de pessoas",
	"versao": "1.0",
	"pessoa": [
		{
			"nome": "joao da silva",
			"profissao": "engenheiro civil",
			"idade": 34
		},
		{
			"nome": "josé da silva",
			"profissao": "médico",
			"idade": 38
		},
		{
			"nome": "maria da silva",
			"profissao": "dentista",
			"idade": 28
		},
	]
}

if __name__ == "__main__":
	servico.run()