def cardiac_risk(patient):

    symptoms = patient["symptoms"]

    score = 0

    if symptoms["chest_pain"]:
        score+=4
    if symptoms["shortness-breath"]:
        score +=2
    if patient["heart_rate"]>110
        score +=2
    if patient["age"] > 60
        score +=1
    return score
