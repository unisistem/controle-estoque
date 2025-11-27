import json

# Nome do arquivo JSON
ARQUIVO_JSON = "estoque.json"

def carregar_estoque():
    """Carrega os dados do arquivo JSON"""
    try:
        with open(ARQUIVO_JSON, 'r') as f:
            dados = json.load(f)
        return dados
    except FileNotFoundError:
        print("Erro: Arquivo estoque.json não encontrado!")
        return None

def salvar_estoque(dados):
    """Salva os dados no arquivo JSON"""
    with open(ARQUIVO_JSON, 'w') as f:
        json.dump(dados, f, indent=4)

def mostrar_estoque(dados):
    """Mostra o estoque atual"""
    print("\n--- ESTOQUE ATUAL ---")
    for produto in dados["estoque"]:
        print(f"Código: {produto['codigoProduto']} - {produto['descricaoProduto']}: {produto['estoque']} unidades")

def mostrar_produtos(dados):
    """Mostra a lista de produtos disponíveis"""
    print("\n--- PRODUTOS DISPONÍVEIS ---")
    for produto in dados["estoque"]:
        print(f"Código: {produto['codigoProduto']} - {produto['descricaoProduto']}")

def encontrar_produto(dados, codigo):
    """Encontra um produto pelo código"""
    for produto in dados["estoque"]:
        if produto["codigoProduto"] == codigo:
            return produto
    return None

def realizar_movimentacao(dados, movimentacoes):
    """Realiza uma movimentação de estoque"""
    print("\n--- NOVA MOVIMENTAÇÃO ---")
    mostrar_produtos(dados)
    
    try:
        codigo = int(input("\nDigite o código do produto: "))
        produto = encontrar_produto(dados, codigo)
        
        if produto is None:
            print("Produto não encontrado!")
            return movimentacoes
        
        print(f"\nProduto selecionado: {produto['descricaoProduto']}")
        print(f"Estoque atual: {produto['estoque']}")
        
        tipo = input("\nTipo de movimentação (E para Entrada / S para Saída): ").upper()
        
        if tipo not in ['E', 'S']:
            print("Tipo inválido! Use E para Entrada ou S para Saída.")
            return movimentacoes
        
        quantidade = int(input("Quantidade: "))
        
        if tipo == 'S' and quantidade > produto['estoque']:
            print("Erro: Quantidade em estoque insuficiente!")
            return movimentacoes
        
        if quantidade <= 0:
            print("Erro: Quantidade deve ser maior que zero!")
            return movimentacoes
        
        # Atualiza o estoque
        if tipo == 'E':
            produto['estoque'] += quantidade
            descricao_mov = f"Entrada de {quantidade} unidades"
        else:
            produto['estoque'] -= quantidade
            descricao_mov = f"Saída de {quantidade} unidades"
        
        # Registra a movimentação
        id_movimentacao = len(movimentacoes) + 1
        movimentacao = {
            "id": id_movimentacao,
            "codigoProduto": codigo,
            "descricao": descricao_mov,
            "quantidade": quantidade,
            "tipo": tipo
        }
        movimentacoes.append(movimentacao)
        
        # Salva as alterações no arquivo JSON
        salvar_estoque(dados)
        
        print(f"\n✅ Movimentação realizada com sucesso!")
        print(f"Novo estoque de {produto['descricaoProduto']}: {produto['estoque']} unidades")
        
        return movimentacoes
        
    except ValueError:
        print("Erro: Digite um número válido!")
        return movimentacoes

def mostrar_movimentacoes(movimentacoes):
    """Mostra o histórico de movimentações"""
    print("\n--- HISTÓRICO DE MOVIMENTAÇÕES ---")
    if not movimentacoes:
        print("Nenhuma movimentação realizada.")
        return
    
    for mov in movimentacoes:
        print(f"ID: {mov['id']} | Produto: {mov['codigoProduto']} | {mov['descricao']}")

def main():
    """Função principal do programa"""
    # Carrega os dados do arquivo JSON
    dados = carregar_estoque()
    if dados is None:
        return
    
    movimentacoes = []
    
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE CONTROLE DE ESTOQUE")
        print("="*50)
        print("1 - Mostrar estoque atual")
        print("2 - Realizar movimentação")
        print("3 - Mostrar histórico de movimentações")
        print("4 - Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            mostrar_estoque(dados)
        elif opcao == "2":
            movimentacoes = realizar_movimentacao(dados, movimentacoes)
        elif opcao == "3":
            mostrar_movimentacoes(movimentacoes)
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()