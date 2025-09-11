import tkinter as tk
from tkinter import messagebox
import random
import webbrowser
import os
import sys
import time

urls = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.wikipedia.org",
    "https://www.reddit.com",
    "https://www.twitter.com",
    "https://www.facebook.com"
]

def abrir_janelas_aleatorias():
    for url in urls:
        webbrowser.open(url)
        time.sleep(1)  # Aguarda 1 segundo entre cada aba (ajuste conforme necessário)
    for i in range(len(urls)):
        webbrowser.open(urls[i])
        time.sleep(1)


def evento_aleatorio():
    escolha = random.randint(1, 6)

    def verificar_escolha(numero):
        if numero == escolha:
            messagebox.showerror("Perdeu!", "😱 Evento indesejado! O computador será desligado!")
            abrir_janelas_aleatorias()
            root.destroy()
            if sys.platform == 'win32':
                os.system("shutdown /s /t 1")
            elif sys.platform.startswith('linux'):
                os.system("shutdown now")
            elif sys.platform == 'darwin':
                os.system("shutdown -h now")
        else:
            messagebox.showinfo("Ufa!", "😌 Você está seguro, por enquanto.")
            evento_aleatorio()

    janela = tk.Toplevel()
    janela.title("Escolha um Número")
    tk.Label(janela, text="Escolha um número entre 1 e 6:").pack(pady=10)

    for i in range(1, 7):
        tk.Button(janela, text=str(i), width=10, command=lambda i=i: [janela.destroy(), verificar_escolha(i)]).pack(pady=5)

def exibir_regras():
    regras = (
        "Regras do Jogo:\n"
        "1. Escolha um número entre 1 e 6.\n"
        "2. Se for o número do evento indesejado, o PC será desligado.\n"
        "3. Se não for, o jogo continua.\n"
        "4. Boa sorte!"
    )
    messagebox.showinfo("Regras", regras)

def sair():
    root.destroy()

root = tk.Tk()
root.title("Jogo de Evento Aleatório")
tk.Label(root, text="Bem-vindo ao Jogo de Evento Aleatório!", font=("Arial", 14)).pack(pady=15)
tk.Button(root, text="Iniciar Jogo", width=20, command=evento_aleatorio).pack(pady=10)
tk.Button(root, text="Ver Regras", width=20, command=exibir_regras).pack(pady=10)
tk.Button(root, text="Sair", width=20, command=sair).pack(pady=10)

root.mainloop()