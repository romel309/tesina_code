import csv
import re
with open('votes/votes_results.csv', 'r', newline='', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    with open('votes/parsed_votes_results.csv', 'w', newline='', encoding="utf8") as p:
        write_vote = csv.writer(p)
        characters_to_eliminate = ["'"]
        max_votes = 5
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
            print("pos: ",is_it_pos,"neg: ",is_it_neg,"neu:",is_it_neu)
            story_wo_url = re.sub(r"http\S+", "", line[0])
            story_wo_characters = story_wo_url.translate({ord(x): '' for x in characters_to_eliminate})
            if is_it_pos >= max_votes:
                write_vote.writerow([story_wo_characters.lower(), "positive"])
            elif is_it_neg >= max_votes:
                write_vote.writerow([story_wo_characters.lower(), "negative"])
  

