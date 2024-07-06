from scripts.carregar_dados import carregar_dados
from scripts.preparar_dados import preparar_dados
from scripts.treinar_modelo import treinar_modelo
from scripts.avaliar_modelo import avaliar_modelo
from scripts.prever_preco import prever_preco

# Caminho para o arquivo de dados
caminho_arquivo = 'dados/casas.csv'

# Carregando os dados
dados = carregar_dados(caminho_arquivo)
if dados is not None:
    # Preparando os dados
    X, y = preparar_dados(dados)
    
    # Treinando o modelo
    modelo, X_test, y_test = treinar_modelo(X, y)
    
    # Avaliando o modelo
    avaliar_modelo(modelo, X_test, y_test)
    
    # Fazendo uma previsão
    prever_preco(modelo, 1500, 3)
