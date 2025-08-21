import numpy as np 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split #para dividir os dados em treino e teste, usando estratificação
import math #funções matemáticas

iris = load_iris()
X = iris.data #aqui carrega as medidas 
y = iris.target #aqui carrega as classes/tipo das flores

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42, stratify=y) #separação para treino 80% e teste 20%

def distancia_euclidiana (p1, p2): #função de cálculo euclidiano dist.
    return math.sqrt(sum((a - b) ** 2 for a, b in zip (p1, p2))) 

def recuperar_caso(X_train, y_train, novo_caso): #aqui faz a recuperação do caso mais próximo
    distancias = [distancia_euclidiana(novo_caso, x) for x in X_train]
    indice_proximo = np.argmin(distancias) #pega o indice menor -caso mais prox.
    return y_train[indice_proximo] #faz o retorno da classe

def rbc_predict(X_train, y_train, X_test): #predição para os casos de teste, onde para cada caso busca o mais parecido no treino
    return [recuperar_caso(X_train, y_train, x) for x in X_test]

y_pred = rbc_predict(X_train, y_train, X_test) #rodando o rbc

acuracia = (np.array(y_pred) == np.array(y_test)).mean() #calculando a acurácia/media de acertos, comparando as previsões com valor de treino 

print(f"total de casos TREINO = {len(X_train)}")
print(f"Total de casos TESTE = {len(X_test)}")
print(f"Acurácia do rbc = {acuracia:.2f}")

