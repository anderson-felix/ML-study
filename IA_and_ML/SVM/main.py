# Support Vector Machine (SVM).

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Carregar o conjunto de dados Iris
iris = load_iris()
X = iris.data  # Características (atributos)
y = iris.target  # Rótulos de classe

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Criar um classificador SVM
svm_classifier = SVC(kernel='linear', C=1)

# Treinar o modelo com os dados de treinamento
svm_classifier.fit(X_train, y_train)

# Fazer previsões com os dados de teste
y_pred = svm_classifier.predict(X_test)

# Avaliar o desempenho do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do modelo: {accuracy}')
