
produtos = {
    "livros": {
        "Python Básico": 50.0,
        "Aprendendo IA": 80.0
    },
    "tablets": {
        "Tablet Samsung": 1200.0,
        "Tablet Lenovo": 900.0
    },
    "fones_de_ouvido": {
        "Fone JBL": 200.0,
        "Fone Sony": 350.0
    }
}

carrinho = []

def comprar(categoria, produto):
    if categoria in produtos and produto in produtos[categoria]:
        preco = produtos[categoria][produto]
        carrinho.append(preco)
        print(f"{produto} adicionado ao carrinho. Preço: R${preco}")
    else:
        print("Produto não encontrado.")

def pagar():
    total = sum(carrinho)
    print(f"Valor total da compra: R${total}")

comprar("livros", "Python Básico")
comprar("tablets", "Tablet Lenovo")
comprar("fones_de_ouvido", "Fone JBL")

pagar()