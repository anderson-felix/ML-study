# ARIMA

# Modelo de previsão de séries temporais,

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_csv('dados.csv')
print(df)

# Ordenando os dados por cnpj, num_nf e code_nf
df.sort_values(by=['cnpj', 'num_nf', 'code_nf'], inplace=True)

# Criando uma nova coluna 'code_nf_pred' para armazenar as previsões
df['code_nf_pred'] = np.nan

# Função para prever os próximos valores de code_nf para um cnpj específico


def prever_code_nf(cnpj):
    user_data = df[df['cnpj'] == cnpj]
    code_nfs = user_data['code_nf'].values

    # Usando um modelo ARIMA simples para prever os próximos valores de code_nf
    modelo = sm.tsa.ARIMA(code_nfs, order=(1, 1, 1))
    modelo_fit = modelo.fit(disp=False)
    forecast = modelo_fit.forecast(steps=1)
    return forecast[0]


cnpjs_unicos = df['cnpj'].unique()
for cnpj in cnpjs_unicos:
    mask = df['cnpj'] == cnpj
    df.loc[mask, 'code_nf_pred'] = prever_code_nf(cnpj)

plt.figure(figsize=(12, 6))
plt.plot(df['num_nf'], df['code_nf'], label='code_nf real', marker='o')
plt.plot(df['num_nf'], df['code_nf_pred'],
         label='code_nf previsto', linestyle='--', marker='x')
plt.xlabel('num_nf')
plt.ylabel('code_nf')
plt.legend()
plt.show()

print(df)
