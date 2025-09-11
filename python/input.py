from pynput import mouse, keyboard
import json
import time

gravar_acoes = []
inicio = time.time()

def tempo_relativo():
    return round(time.time() - inicio, 4)

def on_click(x, y, button, pressed):
    gravar_acoes.append({
        'tipo': 'mouse',
        'acao': 'press' if pressed else 'release',
        'botao': str(button),
        'posicao': (x, y),
        'tempo': tempo_relativo()
    })

def on_press(key):
    gravar_acoes.append({
        'tipo': 'teclado',
        'acao': 'press',
        'tecla': str(key),
        'tempo': tempo_relativo()
    })

def on_release(key):
    if key == keyboard.Key.esc:
        print("Finalizando gravação.")
        return False  # Para o gravador
    gravar_acoes.append({
        'tipo': 'teclado',
        'acao': 'release',
        'tecla': str(key),
        'tempo': tempo_relativo()
    })

# Iniciar gravação
print("Gravação iniciada... (pressione ESC para encerrar)")

with mouse.Listener(on_click=on_click) as ml, keyboard.Listener(on_press=on_press, on_release=on_release) as kl:
    kl.join()
    ml.stop()

# Salva em um arquivo
with open('acoes_gravadas.json', 'w') as f:
    json.dump(gravar_acoes, f, indent=2)

print("Gravação salva em acoes_gravadas.json")