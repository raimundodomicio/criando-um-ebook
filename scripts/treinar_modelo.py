from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dividindo os dados em conjuntos de treino e teste, e treinando o modelo
def treinar_modelo(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    return modelo, X_test, y_test
