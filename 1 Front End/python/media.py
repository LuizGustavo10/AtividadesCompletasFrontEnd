#ENTRADA DE DADOS
nota1 = float(input("Insira a primeira Nota:"))
nota2 = float(input("Insira a segunda Nota:"))
nota3 = float(input("Insira a terceira Nota:"))
nota4 = float(input("Insira a quarta Nota:"))

#PROCESSAMENTO DOS DADOS
notaFinal = (nota1 + nota2 + nota3 + nota4) / 4

#SAÍDA
print("A Nota Final é: ", notaFinal)

if notaFinal < 60:
    print("O Aluno está reprovado!")
elif(notaFinal < 70):
    print("O resultado foi mediano!")
elif(notaFinal < 80):
    print("O Resultado foi muito bom!")
else:
    print("O Aluno foi excelente!")

# def resto_divisao(a, b):
#     return a % b


# # Teste
# a = 10
# b = 3
# print(resto_divisao(a, b))  # Saída esperada: 1



# import random

# def sorteio_numero(minimo, maximo):
#     return random.randint(minimo, maximo)

# # Teste
# minimo = 1
# maximo = 10
# print(sorteio_numero(minimo, maximo))  # Saída esperada: um número entre 1 e 10