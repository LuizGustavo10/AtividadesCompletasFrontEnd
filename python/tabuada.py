#Algoritmo que faz tabuada de número
numero = int(input("Insira um número para a tabuada: "))

# def multiplicar(numero):
#     for i in range(0,11): #percorre de 0 a 10
#         print(numero , "x", i , " = ", numero * i )
    
# multiplicar(numero)


def verificarPar(numero):
    if numero % 2 == 0:
        print("É um número par")
    else:
        print("É um número impar")
        
verificarPar(numero)



# Lista de salgados
salgados = ["Coxinha", "Esfiha", "Pastel", "Empada", "Kibe"]

# Lista de alunos
alunos = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

# Percorrer todos os alunos
for i in range(len(alunos)):
    # Cada aluno compra um salgado pelo índice correspondente
    salgado_escolhido = salgados[i % len(salgados)]  # % evita erro se lista for menor
    print(f"{alunos[i]} comprou {salgado_escolhido}")



    # Lista de salgados
salgados = ["Coxinha", "Esfiha", "Pastel", "Empada", "Kibe"]

# Lista de alunos
alunos = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

# Contador para o while
i = 0

while i < len(alunos):
    salgado_escolhido = salgados[i % len(salgados)]  # repete caso acabem os salgados
    print(f"{alunos[i]} comprou {salgado_escolhido}")
    i += 1  # avança para o próximo aluno





import random

# Lista simples de salgados
salgados = ["Coxinha", "Esfiha", "Pastel", "Kibe", "Empada"]

# Lista de alunos
alunos = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

print("🎯 Sorteio de Salgados\n")

for aluno in alunos:
    salgado_sorteado = random.choice(salgados)
    print(f"{aluno} ganhou {salgado_sorteado}")

print("\n🏁 Sorteio encerrado!")