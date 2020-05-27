import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb

stories = pd.read_csv('../resultados_max/resultados_max_historias.csv', header=None)
stories.columns = ['id_kanji', 'kanji', 'id_story', 'story', 'stars', 'sentiment', 'num_words']
pc = stories.drop(['id_kanji', 'kanji', 'id_story', 'story'], axis=1)
pos = pc.loc[pc['sentiment'] > 0, ['stars','sentiment','num_words']]
neg = pc.loc[pc['sentiment'] < 0 , ['stars','sentiment','num_words']]
pos_index = pos.index
number_of_rows_pos = len(pos_index)
neg_index = neg.index
number_of_rows_neg = len(neg_index)

count_row = pc.shape[0]
print("Total de historias", count_row)
print("Positivas", count_row)
total_pos = pos['stars'].sum()
print("Positivas", total_pos)
total_neg = neg['stars'].sum()
print("Negativas", total_neg)



plt.scatter(neg['sentiment'], neg['stars'], c="red")
plt.title("Historias Negativas")
plt.xlabel("predicciones")
plt.ylabel("estrellas")
#plt.show()
plt.savefig('scatter_negativas.png')

plt.scatter(neg['sentiment'], neg['stars'], c="green")
plt.title("Historias Positivas")
plt.xlabel("predicciones")
plt.ylabel("estrellas")
#plt.show()
plt.savefig('scatter_positivas.png')

pearsoncorr = pos.corr(method='pearson')
sb.heatmap(pearsoncorr, 
            xticklabels=pearsoncorr.columns,
            yticklabels=pearsoncorr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5)

#plt.show()
plt.savefig('corelacion_positivas.png')


pearsoncorr = neg.corr(method='pearson')
sb.heatmap(pearsoncorr, 
            xticklabels=pearsoncorr.columns,
            yticklabels=pearsoncorr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5)

#plt.show()
plt.savefig('correlacion_negativas.png')