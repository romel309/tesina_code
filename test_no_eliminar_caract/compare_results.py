import csv
with open('results.csv', 'r') as f:
    csv_reader = csv.reader(f)
    #vader
    count_vader = 0
    pos_va = 0
    neg_va = 0
    #blob
    count_blob = 0
    pos_blob = 0
    neg_blob = 0
    #ibm
    count_ibm = 0
    pos_ibm = 0
    neg_ibm = 0
    #votes results
    votes_res = 4
    total_pos = 0
    total_neg = 0
    for i, line in enumerate(csv_reader):
        if line[votes_res] == "positive":
            total_pos = total_pos +1
        elif line[votes_res] == "negative":
            total_neg = total_neg +1
        #vader
        if line[1] == line[votes_res]:
            count_vader = count_vader+1
            if line[4] == "positive":
                pos_va = pos_va+1
            elif line[votes_res] == "negative":
                neg_va = neg_va+1
        #blob
        if line[2] == line[votes_res]:
            count_blob = count_blob+1
            if line[votes_res] == "positive":
                pos_blob = pos_blob+1
            elif line[votes_res] == "negative":
                neg_blob = neg_blob+1
        #ibm_max
        if line[3] == line[4]:
            count_ibm = count_ibm+1
            if line[votes_res] == "positive":
                pos_ibm = pos_ibm+1
            elif line[votes_res] == "negative":
                neg_ibm = neg_ibm+1
    print("Exactitud vader: ", count_vader/(i+1),"\nExactitud positivas vader: ", pos_va/total_pos, "\nExactitud negativas vader: ", neg_va/total_neg)
    print("Exactitud blob: ", count_blob/(i+1),"\nExactitud positivas blob: ", pos_blob/total_pos, "\nExactitud negativas blob: ", neg_blob/total_neg)
    print("Exactitud ibm_max:", count_ibm/(i+1),"\nExactitud positivas ibm: ", pos_ibm/total_pos, "\nExactitud negativas ibm: ", neg_ibm/total_neg)
    f= open("Exactitudes.txt","w+")
    f.write("Exactitud vader: " + str(count_vader/(i+1)) +"\nExactitud positivas vader: " + str(pos_va/total_pos) + "\nExactitud negativas vader: "+str(neg_va/total_neg))
    f.write("Exactitud blob: "+str(count_blob/(i+1))+"\nExactitud positivas blob: "+str(pos_blob/total_pos)+"\nExactitud negativas blob: "+str(neg_blob/total_neg))
    f.write("Exactitud ibm_max:"+str(count_ibm/(i+1))+"\nExactitud positivas ibm: "+str(pos_ibm/total_pos)+"\nExactitud negativas ibm: "+str(neg_ibm/total_neg))