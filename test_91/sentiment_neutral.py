import requests
import json
from textblob import TextBlob
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

with open('results.csv', 'w', newline='', encoding="utf8") as p:
		write_result = csv.writer(p) 

with open('votes/parsed_votes_results.csv', 'r', encoding="utf8") as f:
    with open('results.csv', 'w', newline='', encoding="utf8") as p:
        write_result = csv.writer(p) 
        csv_reader = csv.reader(f)
        #vader
        vneg = 0
        vpos = 0
        vneu = 0
        # blob
        bneg = 0
        bpos = 0
        bneu = 0
        # ibm_max
        ibm_pos = 0
        ibm_neg = 0
        for i, line in enumerate(csv_reader):
            vs = analyzer.polarity_scores(line[0])
            analysis_bob = TextBlob(line[0])
            words_in_story = len(line[0].split())
            #Vader
            if vs['compound'] >= 0.05:
                result_sentiment = "positive"
                vpos = vpos+1
            elif vs['compound'] <= -0.05:
                result_sentiment = "negative"
                vneg = vneg+1
            else:
                result_sentiment = "neutral"
                vneu = vneu+1
            #Bob
            if analysis_bob.sentiment.polarity < 0:
                bneg = bneg+1
                bob_result_sentiment = "negative"
            elif analysis_bob.sentiment.polarity > 0:
                bpos = bpos+1
                bob_result_sentiment = "positive"
            else:
                bneu = bneu+1
                bob_result_sentiment = "neutral"
            # Max
            url = "http://192.168.99.100:5000/model/predict"
            payload = {
                'text': [line[0]]
            }
            r = requests.post(url,json=payload)
            pred = r.json().get('predictions').pop()
            if pred['positive'] > pred['negative']:
                ibm_pos = ibm_pos+1
                ibm_result_sentiment = "positive"
            elif pred['negative'] > pred['positive']:
                ibm_neg = ibm_neg+1
                ibm_result_sentiment = "negative"
            else:
                ibm_result_sentiment = "neutral"
            write_result.writerow([line[0], result_sentiment, bob_result_sentiment,ibm_result_sentiment,line[1]])
        print("Vader positivos: ",vpos," negativos: ",vneg," neutrales: ",vneu)
        print("Bob positivos: ",bpos," negativos: ",bneg," neutrales: ",bneu)
        print("IBM-MAX positivos: ",ibm_pos," negativos: ",ibm_neg)

            
