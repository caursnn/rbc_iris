"""
 RBC Raciocínio baseado em Casos com Iris Dataset

RBC é uma forma de resolver problemas usando exemplos que já aconteceram.  
Em vez de treinar um modelo ou criar várias regras, a ideia é que dado um novo caso, o RBC olha para os casos antigos e pega qual for mais parecido para usar como resposta.

Explicação da Atividade
Aqui eu usei o RBC no conjunto de dados Iris, tendo medidas de três tipos de flores. Primeiro, separei 80% dos dados para treino (casos existentes) e deixei 20% para teste (casos novos). Depois, para cada flor de teste calculei a distância euclidiana até todas as flores do treino e escolhi a mais próxima. A espécie dessa flor mais próxima foi usada como resposta para o novo caso. No final, calculei a acurácia que mostra quantas previsões o RBC acertou em comparação com as classes reais.

Cauana Rosin Ghizzi
"""

