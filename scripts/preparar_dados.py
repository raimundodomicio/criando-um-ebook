# Separando as características (features) do alvo (target)
def preparar_dados(dados):
    X = dados[['area', 'quartos']]
    y = dados['preco']
    return X, y
