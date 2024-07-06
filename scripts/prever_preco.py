# Fazendo previsões com o modelo treinado
def prever_preco(modelo, area, quartos):
    nova_casa = [[area, quartos]]
    preco_previsto = modelo.predict(nova_casa)
    print(f"O preço previsto para a nova casa é: ${preco_previsto[0]:.2f}")
