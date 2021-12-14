# <font color='blue'>Marchine Learning - Previsão Diaria do BCTUSD</font>

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Base de dados do BCTUSD no período diário 
# ATUALIZAÇÃO DA BASE DE DADOS: 13/11/2021

bctusd = pd.read_csv('BCTUSD_D1.csv', sep = '\t')

# Listas para treinar o algoritmo

abertura = []
for a in bctusd.Open:
    abertura += [[a]]

fechamento = []
for f in bctusd.Close:
    fechamento +=[[f]]
    
maxima = []
for m in bctusd.High:
    maxima +=[[m]]
    
minima = []
for n in bctusd.Low:
    minima +=[[n]]
    
data = []
for d in bctusd.Time:
    data +=[[d]]

# Listas para gerar o gráfico   
x = []
for mm in bctusd.Time:
    x +=[mm]
    
y = []
for nn in bctusd.Close:
    y +=[nn]

# Criando o LinearRegression()
modeloFechamento = LinearRegression()
modeloMaxima = LinearRegression()
modeloMinima = LinearRegression()

# Treinando o modelo
modeloFechamento.fit(abertura, fechamento)
modeloMaxima.fit(abertura, maxima)
modeloMinima.fit(abertura, minima)
#print("Modelo Treinado")

# Prevendo o preço de fechamento, informe o preço de abertura
precoAbertura = float(input("Informe o preço de abertura do BCTUSD: "))
previsaoFechamento = modeloFechamento.predict([[precoAbertura]])
previsaoMaxima = modeloMaxima.predict(([[precoAbertura]]))
previsaoMinima = modeloMinima.predict(([[precoAbertura]]))
#variacao = var(precoabertura, previsao)

print("\nPrevisão de FECHAMENTO do BCTUSD: U$%.2f" % previsaoFechamento)
print("\nPrevisão da MÁXIMA do BCTUSD: U$%.2f" % previsaoMaxima)
print("\nPrevisão da MINIMA do BCTUSD: U$%.2f" % previsaoMinima)

# Gráfico do BCTUSD
plt.plot(x, y)
plt.xlabel('PERÍODO')
plt.ylabel('PREÇO U$')
plt.title('BCTUSD TIME FRAME D1')
plt.show()