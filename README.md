Sistema de Controle de Estoque
Sistema simples para gerenciamento de movimentações de estoque, desenvolvido em Python.

📋 Funcionalidades
Visualizar estoque atual - Lista todos os produtos com seus códigos e quantidades

Realizar movimentações - Entrada (E) e Saída (S) de produtos do estoque

Histórico de movimentações - Registro completo de todas as operações realizadas

Persistência de dados - Os dados são salvos automaticamente em arquivo JSON

🚀 Como usar
Pré-requisitos
Python 3.x instalado

Configuração inicial
Crie o arquivo estoque.json na mesma pasta do programa com o seguinte conteúdo:

json
{
    "estoque": [
        {
            "codigoProduto": 101,
            "descricaoProduto": "Caneta Azul",
            "estoque": 150
        },
        {
            "codigoProduto": 102,
            "descricaoProduto": "Caderno Universitário",
            "estoque": 75
        },
        {
            "codigoProduto": 103,
            "descricaoProduto": "Borracha Branca",
            "estoque": 200
        },
        {
            "codigoProduto": 104,
            "descricaoProduto": "Lápis Preto HB",
            "estoque": 320
        },
        {
            "codigoProduto": 105,
            "descricaoProduto": "Marcador de Texto Amarelo",
            "estoque": 90
        }
    ]
}
Execute o programa:

bash
python estoque.py

📝 Menu Principal

==================================================
SISTEMA DE CONTROLE DE ESTOQUE
==================================================
1 - Mostrar estoque atual
2 - Realizar movimentação
3 - Mostrar histórico de movimentações
4 - Sair

🔄 Fluxo de Movimentação
Selecione a opção 2 - Realizar movimentação

Escolha o produto pelo código

Selecione o tipo:

E para Entrada (aumenta estoque)

S para Saída (diminui estoque)

Informe a quantidade

Confirmação automática com novo saldo do estoque

⚠️ Validações
Verifica se o produto existe

Impede saídas maiores que o estoque disponível

Bloqueia quantidades negativas ou zero

Valida tipos de movimentação (apenas E/S)

💾 Estrutura de Dados
Arquivo estoque.json
json
{
    "estoque": [
        {
            "codigoProduto": 101,
            "descricaoProduto": "Caneta Azul",
            "estoque": 150
        }
    ]
}
Movimentações (em memória)
Cada movimentação registra:

ID único sequencial

Código do produto

Descrição da operação

Quantidade movimentada

Tipo (E/S)

📊 Exemplo de Uso
text
--- ESTOQUE ATUAL ---
Código: 101 - Caneta Azul: 150 unidades

--- NOVA MOVIMENTAÇÃO ---
Digite o código do produto: 101
Tipo de movimentação (E para Entrada / S para Saída): S
Quantidade: 50

✅ Movimentação realizada com sucesso!
Novo estoque de Caneta Azul: 100 unidades
🛠️ Tecnologias
Python 3.x

JSON para persistência de dados

Estrutura modular com funções específicas
