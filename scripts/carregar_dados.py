import pandas as pd

# Carregando os dados do arquivo CSV
def carregar_dados(caminho_arquivo):
    try:
        dados = pd.read_csv(caminho_arquivo)
        return dados
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. Verifique o caminho do arquivo.")
        return None
