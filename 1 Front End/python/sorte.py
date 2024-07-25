import random
import os
import sys
import time
import webbrowser

#prmeiro terminar o imc
#prmeiro terminar o imc
#prmeiro terminar o imc
#prmeiro terminar o imc


#prmeiro terminar o imc
#prmeiro terminar o imc
#prmeiro terminar o imc

#prmeiro terminar o imc
#prmeiro terminar o imc
#prmeiro terminar o imc


#prmeiro terminar o imc
#prmeiro terminar o imc
#prmeiro terminar o imc

#prmeiro terminar o imc
#prmeiro terminar o imc
#prmeiro terminar o imc
#prmeiro terminar o imc



def abrir_janelas_aleatorias():
    urls = [
        "https://www.google.com",
        "https://www.youtube.com",
        "https://www.wikipedia.org",
        "https://www.reddit.com",
        "https://www.twitter.com",
        "https://www.facebook.com"
    ]
    
    for _ in range(5):  # Abrir 5 janelas aleatórias
        url = random.choice(urls)
        webbrowser.open(url)

def evento_aleatorio():
    num_opcoes = 6
    escolha_indesejada = random.randint(1, num_opcoes)

    try:
        escolha = int(input(f"Escolha um número entre 1 e {num_opcoes}: "))
        if escolha < 1 or escolha > num_opcoes:
            raise ValueError("Número fora do intervalo permitido.")
            
    except ValueError as e:
        print(f"Entrada inválida: {e}. Tente novamente.")
        evento_aleatorio()

    if escolha == escolha_indesejada:
        print("Ops! O computador abrirá janelas aleatórias e será desligado.")
        print("""
⠀👻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

        time.sleep(5)
        abrir_janelas_aleatorias()
        if sys.platform == 'win32':
            os.system("shutdown /s /t 1")  # Para Windows
        elif sys.platform == 'linux' or sys.platform == 'linux2':
            os.system("shutdown now")  # Para Linux
        elif sys.platform == 'darwin':
            os.system("shutdown -h now")  # Para macOS
        sys.exit()
    else:
        print("Você está seguro, por enquanto.")
        print("""
        ⠀(づ｡◕‿‿◕｡)づ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        """)

        evento_aleatorio()



        # playsound('click_sound.mp3')  # Certifique-se de que você tem um arquivo de som 'click_sound.mp3'

def exibir_regras():
    print("""
Regras do Jogo de Evento Aleatório:
1. Você deve escolher um número entre 1 e 6.
2. Se você escolher o número que corresponde ao evento indesejado, o computador abrirá janelas aleatórias e será desligado.
3. Se você escolher um número diferente, o jogo continuará.
4. O jogo continua até que você decida parar ou escolha o número do evento indesejado.
    """)
    menu_principal()

def menu_principal():
        print("\nMenu Principal")
        print("1. Iniciar Jogo")
        print("2. Ver Regras")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            evento_aleatorio()
        elif escolha == '2':
            exibir_regras()
        elif escolha == '3':
            print("Saindo do jogo. Até mais!")
            
        else:
            print("Opção inválida. Tente novamente.")

print("Bem-vindo ao Jogo de Evento Aleatório!")
menu_principal()