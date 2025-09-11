from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Abre o navegador
driver = webdriver.Chrome()

# Acessa o WhatsApp Web
driver.get("https://web.whatsapp.com/")
input("Escaneie o QR Code e pressione Enter...")

# Nome do contato ou grupo
contato = "Christian Garcia"

# Mensagem
mensagem = "Olá, esta é uma mensagem automática do Python!"

# Procura contato
search_box = driver.find_element("xpath", "//div[@contenteditable='true'][@data-tab='3']")
search_box.send_keys(contato)
time.sleep(2)
search_box.send_keys(Keys.ENTER)

# Envia mensagem
msg_box = driver.find_element("xpath", "//div[@contenteditable='true'][@data-tab='10']")
msg_box.send_keys(mensagem)
msg_box.send_keys(Keys.ENTER)

print("Mensagem enviada com sucesso!")