# ==========================================
# SISTEMA DE CONTROLE DE CAIXAS
# ==========================================

# Banco de dados dos produtos
produtos = {
    "1001": {
        "nome": "Arroz",
        "lote": "AR123",
        "validade": "10/2027"
    },

    "1002": {
        "nome": "Feijão",
        "lote": "FE456",
        "validade": "08/2027"
    },

    "1003": {
        "nome": "Macarrão",
        "lote": "MA789",
        "validade": "12/2027"
    }
}

# Banco de dados das caixas
caixas = {}


# ==========================================
# 1. INTRODUÇÃO / ENTRADA
# ==========================================

def criar_caixa():

    print("\n===== CADASTRO DA CAIXA =====")

    codigo_caixa = input("Bipe o código da caixa: ")

    # Verifica se a caixa já existe
    if codigo_caixa in caixas:
        print("Essa caixa já está cadastrada.")
        return

    # Cria uma lista para armazenar os produtos
    caixas[codigo_caixa] = []

    print("\nCaixa", codigo_caixa, "criada!")

    # Adicionando produtos
    while True:

        codigo_produto = input(
            "\nBipe o código do produto "
            "(0 para finalizar): "
        )

        if codigo_produto == "0":
            break

        # Verifica se o produto está cadastrado
        if codigo_produto not in produtos:
            print("Produto não cadastrado!")
            continue

        quantidade = int(input("Digite a quantidade: "))

        produto = produtos[codigo_produto]

        # Cria o registro do produto
        item = {
            "codigo": codigo_produto,
            "nome": produto["nome"],
            "quantidade": quantidade,
            "lote": produto["lote"],
            "validade": produto["validade"]
        }

criar_caixa()
