# Estoque de ingredientes
estoque = {
    "massa": 10,         # 10 massas disponíveis
    "queijo": 20,        # 20 porções de queijo
    "calabresa": 15,     # 15 porções de calabresa
    "bacon": 10,         # 10 porções de bacon
    "molho": 20          # 20 porções de molho
}

# Receitas de pizza
receitas = {
    "marguerita": {"massa":1, "queijo":2, "molho":1},
    "calabresa": {"massa":1, "queijo":2, "calabresa":2, "molho":1},
    "bacon": {"massa":1, "queijo":2, "bacon":2, "molho":1}
}

def mostrar_estoque():
    print("\nEstoque atual:")
    for ingrediente, quantidade in estoque.items():
        print(f"{ingrediente}: {quantidade}")

def pedir_pizza():
    print("\nPizzas disponíveis:")
    for pizza in receitas.keys():
        print(f"- {pizza}")
    escolha = input("Qual pizza deseja pedir? ").lower()
    
    if escolha not in receitas:
        print("Pizza não disponível.")
        return
    
    receita = receitas[escolha]
    
    # Verificar estoque
    for ingrediente, quantidade in receita.items():
        if estoque.get(ingrediente,0) < quantidade:
            print(f"Não há estoque suficiente de {ingrediente} para fazer esta pizza.")
            return
    
    # Reduzir estoque
    for ingrediente, quantidade in receita.items():
        estoque[ingrediente] -= quantidade
    
    print(f"Pizza {escolha} feita com sucesso!")

# Loop principal
while True:
    print("\n1 - Mostrar estoque")
    print("2 - Pedir pizza")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        mostrar_estoque()
    elif opcao == "2":
        pedir_pizza()
    elif opcao == "3":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida!")
