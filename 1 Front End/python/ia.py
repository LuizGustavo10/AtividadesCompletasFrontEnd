from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Carregar modelo leve (distilgpt2)
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Função para gerar resposta
def gerar_resposta(pergunta, max_length=100):
    # Codifica a entrada
    inputs = tokenizer.encode(pergunta, return_tensors="pt")
    
    # Gera resposta
    outputs = model.generate(
        inputs, 
        max_length=max_length, 
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.8
    )
    
    resposta = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return resposta

# Exemplo de uso
while True:
    pergunta = input("Você: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        break
    resposta = gerar_resposta(pergunta)
    print("GPT leve: ", resposta)