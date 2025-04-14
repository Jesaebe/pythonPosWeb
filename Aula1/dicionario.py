cadastro = {
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
	# print(f"{cadastro}")

	descricao = cadastro["descricao"]
	print(f"descricao do cadastro: {descricao}")

	