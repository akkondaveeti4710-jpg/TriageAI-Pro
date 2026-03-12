def infection_risk(patient)

    symptoms = patient["symptoms"]
    score = 0

    if symptoms["fever"]:
        score +=3

    if patient["temp"] > 39
        score +=3
    if patient["heart_rate"] > 110
        score +=2
    if patient["bp_sys"] < 90:
        score += 2
    return score
