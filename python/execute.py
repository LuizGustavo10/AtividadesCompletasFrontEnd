from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key
import json
import time
import ast

# Carrega ações
with open('acoes_gravadas.json', 'r') as f:
    acoes = json.load(f)

mouse = MouseController()
teclado = KeyboardController()

print("Reproduzindo ações...")

inicio = time.time()

for i, acao in enumerate(acoes):
    if i > 0:
        # Aguarda o tempo relativo entre eventos
        delay = acoes[i]['tempo'] - acoes[i - 1]['tempo']
        time.sleep(delay)

    if acao['tipo'] == 'mouse':
        pos = tuple(acao['posicao'])
        mouse.position = pos
        botao = Button.left if 'left' in acao['botao'] else Button.right
        if acao['acao'] == 'press':
            mouse.press(botao)
        else:
            mouse.release(botao)

    elif acao['tipo'] == 'teclado':
        tecla = acao['tecla']
        try:
            tecla_eval = eval(tecla) if 'Key.' in tecla else tecla.strip("'")
        except:
            tecla_eval = tecla.strip("'")
        if acao['acao'] == 'press':
            teclado.press(tecla_eval)
        else:
            teclado.release(tecla_eval)

print("Reprodução finalizada.")