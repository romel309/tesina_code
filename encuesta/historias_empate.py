import csv
import re
with open('votes_results.csv', 'r', newline='', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    with open('historias_empatadas/historias_empate.csv', 'w', newline='', encoding="utf8") as p:
        write_vote = csv.writer(p)
        characters_to_eliminate = ["'",":","/","(",")","[","]",";","_","="]
        max_votes = 5
        final_pos = 0
        final_neg = 0
        final_neu = 0
        mixed = 0
        for line in csv_reader:
            is_it_pos = 0
            is_it_neg = 0
            is_it_neu = 0
            for i in range(0, len(line)):
                if  line[i] == "Positivo":
                    is_it_pos=is_it_pos+1
                elif line[i] == "Negativo":
                    is_it_neg=is_it_neg+1
                elif line[i] == "Neutral":
                    is_it_neu=is_it_neu+1
            story_wo_url = re.sub(r"http\S+", "", line[0])
            story_wo_characters = story_wo_url.translate({ord(x): '' for x in characters_to_eliminate})
            if is_it_pos > is_it_neg and is_it_pos > is_it_neu:
                #write_vote.writerow([story_wo_characters, "positive"])
                final_pos+=1
                #print("pos: ",is_it_pos,"neg: ",is_it_neg,"neu:",is_it_neu,"mayoria positivo")
            elif is_it_neg > is_it_pos and is_it_neg > is_it_neu:
                #write_vote.writerow([story_wo_characters, "negative"])
                final_neg+=1
                #print("pos: ",is_it_pos,"neg: ",is_it_neg,"neu:",is_it_neu,"mayoria negativo")
            elif is_it_neu > is_it_pos and is_it_neu > is_it_neg:
                #write_vote.writerow([story_wo_characters, "neutral"])
                final_neu+=1
                #print("pos: ",is_it_pos,"neg: ",is_it_neg,"neu:",is_it_neu,"mayoria neutral")
            else:
                mixed+=1
                write_vote.writerow(line)
                print("pos: ",is_it_pos,"neg: ",is_it_neg,"neu:",is_it_neu,"mixed")
        print("total pos: ",final_pos,"total neg: ",final_neg,"neu:",final_neu,"mixed", mixed)

