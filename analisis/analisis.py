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
count_row_p = pos.shape[0]
count_row_n = neg.shape[0]
print("Total de historias", count_row)
print("Total de historias positivas", count_row_p)
print("Total de historias negativas", count_row_n)
total_pos = pos['stars'].sum()
print("Positivas", total_pos)
total_neg = neg['stars'].sum()
print("Negativas", total_neg)


noventa = pos.loc[pc['sentiment'] > 0.9, ['stars','sentiment','num_words']]

print("Más de 90 positivos", pos.loc[pos['sentiment'] >= 0.9, ['sentiment']].shape[0])
print("Más de 80 positivos", pos.loc[(pos['sentiment'] < 0.9 ) & (pos['sentiment'] >= 0.8), ['sentiment']].shape[0])
print("Más de 70 positivos", pos.loc[(pos['sentiment'] < 0.8 ) & (pos['sentiment'] >= 0.7), ['sentiment']].shape[0])
print("Más de 60 positivos", pos.loc[(pos['sentiment'] < 0.7 ) & (pos['sentiment'] >= 0.6), ['sentiment']].shape[0])
print("Más de 50 positivos", pos.loc[(pos['sentiment'] < 0.6 ) & (pos['sentiment'] >= 0.5), ['sentiment']].shape[0])


print("Más de 90 negativos", neg.loc[neg['sentiment'] <= -0.9, ['sentiment']].shape[0])
print("Más de 80 negativos", neg.loc[(neg['sentiment'] > -0.9 ) & (neg['sentiment'] <= -0.8), ['sentiment']].shape[0])
print("Más de 70 negativos", neg.loc[(neg['sentiment'] > -0.8 ) & (neg['sentiment'] <= -0.7), ['sentiment']].shape[0])
print("Más de 60 negativos", neg.loc[(neg['sentiment'] > -0.7 ) & (neg['sentiment'] <= -0.6), ['sentiment']].shape[0])
print("Más de 50 negativos", neg.loc[(neg['sentiment'] > -0.6 ) & (neg['sentiment'] <= -0.5), ['sentiment']].shape[0])





plt.scatter(pos['sentiment'], pos['stars'], c="green")
plt.title("Historias Positivas")
plt.xlabel("predicciones")
plt.ylabel("estrellas")
plt.show()
#plt.savefig('scatter_positivas.png')


plt.scatter(neg['sentiment'], neg['stars'], c="red")
plt.title("Historias Negativas")
plt.xlabel("predicciones")
plt.ylabel("estrellas")
plt.show()
#plt.savefig('scatter_negativas.png')

pearsoncorr = pos.corr(method='pearson')
sb.heatmap(pearsoncorr, 
            xticklabels=pearsoncorr.columns,
            yticklabels=pearsoncorr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5)

#plt.show()
#plt.savefig('corelacion_positivas.png')


pearsoncorr = neg.corr(method='pearson')
sb.heatmap(pearsoncorr, 
            xticklabels=pearsoncorr.columns,
            yticklabels=pearsoncorr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5)

#plt.show()
#plt.savefig('correlacion_negativas.png')

#pc.to_csv (r'agrupaciones\\historias_agrupadas.csv', index = False, header=False)
#pos.to_csv (r'agrupaciones\\historias_positivas.csv', index = False, header=False)
#neg.to_csv (r'agrupaciones\\historias_negativas.csv', index = False, header=False)