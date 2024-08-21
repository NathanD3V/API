# Armazenamento 
residuos = {}

#  adicionar um resíduo
def adicionar_residuo(residuo, estado, quantidade=1):
    global residuos
    
    # quantidade total após a adição
    nova_quantidade_total = sum(item['quantidade'] for item in residuos.values()) + quantidade
    
    # Verifica se excede o limite de 100
    if nova_quantidade_total > 100:
        print("Limite máximo de quantidade atingido. Não é possível adicionar mais itens.")
        return
    
    # Verifica se o resíduo 
    if residuo in residuos:
        residuos[residuo]['quantidade'] += quantidade
    else:
        residuos[residuo] = {'estado': estado, 'quantidade': quantidade}
    print(f"Resíduo {residuo} adicionado com sucesso. Quantidade: {residuos[residuo]['quantidade']}")

# remover 
def remover_residuo(residuo):
    global residuos
    if residuo in residuos:
        del residuos[residuo]
        print(f"Resíduo {residuo} removido com sucesso.")
    else:
        print("Resíduo não encontrado.")

#  visualizar o status 
def visualizar_status():
    global residuos
    if not residuos:
        print("Não há resíduos cadastrados.")
    else:
        for residuo, item in residuos.items():
            print(f"Resíduo: {residuo}, Estado: {item['estado']}, Quantidade: {item['quantidade']}")

# Loop do menu
while True:
    print("\nMenu:")
    print("1. Adicionar Resíduo")
    print("2. Remover Resíduo")
    print("3. Visualizar Status")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        residuo = input("Digite qual é o resíduo: ")
        estado = input("Digite o estado do resíduo: ")
        quantidade = int(input("Digite a quantidade do resíduo (ou 1 para apenas um): "))
        adicionar_residuo(residuo, estado, quantidade)
    elif opcao == "2":
        residuo = input("Digite o código do resíduo a ser removido: ")
        remover_residuo(residuo)
    elif opcao == "3":
        visualizar_status()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
