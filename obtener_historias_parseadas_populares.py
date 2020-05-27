import csv
import pandas as pd
from langdetect import detect
import re
from string import digits

#Invertir csv
df = pd.read_csv("historias_con_score.csv", header=None)

df.columns = ['id_kanji', 'kanji', 'id_story', 'story', 'popul']

invert = df.iloc[::-1]

invert.to_csv (r'csvs/historias_con_score_invertidas.csv', index = False, header=False)

# Parsear historias
with open('csvs\\historias_con_score_invertidas.csv', 'r', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('csvs\\historias_ivertidas_parseadas_populares.csv', 'w', newline='', encoding="utf8") as p:
        write_story = csv.writer(p)
        characters_to_eliminate = ['*','{','}','-','"','#',":","/","(",")","[","]",";","_"]
        remove_digits = str.maketrans('', '', digits)
        id_actual = 0
        id_min = 0
        for line in csv_reader:
            if id_actual != line[0]:
                id_actual = line[0]
                id_min+=1
            else:
                if id_min == 1 and id_actual == line[0]:
                    id_min=0
                else:
                    story_wo_url = re.sub(r"http\S+", "", line[3])
                    story_to_detect = story_wo_url.translate(remove_digits)
                    if story_to_detect != "" and re.search('[a-zA-Z]', story_to_detect):
                        if detect(story_to_detect) == "en":
                            story_wo_characters = story_to_detect.translate({ord(x): '' for x in characters_to_eliminate})
                            story_wo_special_characters = re.sub("([^\x00-\x7F])+"," ",story_wo_characters)
                            write_story.writerow([line[0],line[1],line[2]," ".join(story_wo_special_characters.split()),line[4]])
            

hipp = pd.read_csv("csvs\\historias_ivertidas_parseadas_populares.csv", header=None)

hipp.columns = ['id_kanji', 'kanji', 'id_story', 'story', 'popul']

hipp_invert = hipp.iloc[::-1]

hipp_invert.to_csv (r'historias_populares\\historias_populares.csv', index = False, header=False)

