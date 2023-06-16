#entrada de dados
precoAlcool = float(input("Insira o valor do alcool: "))
precoGasolina = float(input("Insira o valor da Gasolina: "))

#processamento
resultado = precoAlcool / precoGasolina

#saída
print(resultado)

if resultado > 0.7:
    print("abasteça com gasolina")
else:
    print("Abasteça com alcool")

