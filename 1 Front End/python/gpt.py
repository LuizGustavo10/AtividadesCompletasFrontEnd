from transformers import pipeline

# Cria o gerador de texto (usando o modelo GPT-2)
gerador = pipeline("text-generation", model="pierreguillou/gpt2-small-portuguese")

# Texto inicial (prompt)
inicio = "Era uma vez um robô que"

# Gera texto
resposta = gerador(inicio, max_length=50, num_return_sequences=1)

# Mostra o resultado
print("História:", resposta[0]['generated_text'])
