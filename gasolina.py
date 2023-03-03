import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('./gasolina.csv')

sns.set_style('darkgrid')
sns.lineplot(data=dados, x='dia', y='venda', color='red' )

plt.title('Preço médio da gasolina') 
plt.xlabel('Dia') 
plt.ylabel('Preço (R$)') 

plt.savefig('./gasolina.png')