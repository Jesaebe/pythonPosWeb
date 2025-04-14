def somar(numero_a, numero_b):
	resultado = numero_a + numero_b

	return resultado

def somar_e_multiplicar(numero_a, numero_b):
	soma = numero_a + numero_b
	multiplicacao = numero_a * numero_b

	return soma, multiplicacao

if __name__ == "__main__":
	resultado = somar(2, 3)
	print(f"resultado = {resultado}")
	
	soma, multiplicacao = somar_e_multiplicar(3, 4)
	print(f"soma = {soma}")
	print(f"multiplicacao = {multiplicacao}")