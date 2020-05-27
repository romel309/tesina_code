import requests
import json
import csv
#docker run -it -p 5000:5000 codait/max-text-sentiment-classifier
#5305 pos, 4840 neg

with open('historias_populares\\historias_populares.csv', 'r', encoding="utf8") as f:
    with open('resultados_max/resultados_max_historias.csv', 'w', newline='', encoding="utf8") as p:
        write_result = csv.writer(p) 
        csv_reader = csv.reader(f)
        # ibm_max
        ibm_pos = 0
        ibm_neg = 0
        for i, line in enumerate(csv_reader):
            words_in_story = len(line[3].split())
            # Max
            url = "http://192.168.99.100:5000/model/predict"
            payload = {
                'text': [line[3]]
            }
            r = requests.post(url,json=payload)
            pred = r.json().get('predictions').pop()
            if pred['positive'] > pred['negative']:
                ibm_pos = ibm_pos+1
                ibm_result_sentiment = 1*pred['positive']
            else:
                ibm_neg = ibm_neg+1
                ibm_result_sentiment = -1*pred['negative']
            write_result.writerow([line[0], line[1], line[2],line[3],line[4],ibm_result_sentiment,words_in_story])
    print("IBM-MAX positivos: ",ibm_pos," negativos: ",ibm_neg)
