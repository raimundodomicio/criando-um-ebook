# Avaliando a acurácia do modelo
def avaliar_modelo(modelo, X_test, y_test):
    score = modelo.score(X_test, y_test)
    print(f"Acurácia do modelo: {score * 100:.2f}%")
