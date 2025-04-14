frutas = ["banana","abacaxi","uva","manga","goiaba","maçã"]

if __name__ == "__main__":
	print(f"Lista de Frustas: {frutas}")

	# for fruta in frutas:
	# 	print(f"{fruta} é uma fruta")

	# frutas.append("melância")

	# for fruta in frutas:
	# 	print(f"{fruta} é uma fruta")

	frutas.append("melância")

	for posicao, fruta in enumerate(frutas):
		print(f"{fruta} é uma fruta na posição {posicao}")
