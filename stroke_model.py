def stroke_risk(patient):

    symptoms = patient["symptoms"]

    score = 0

    if symptoms["confusion"]:
        score += 3

    if symptoms["sever_headache"]:
        score +=3
    if symptoms["dizziness"]:
        score +=2
    if patient["age"] > 60
        score +=1
    return score
