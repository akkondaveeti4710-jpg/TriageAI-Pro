def analyze_vitals(patient):

    score=0

    if patient["heart_rate"] > 110:
        score +=2
    if patient["bp_sys"] < 90:
        score+=3
    if patient["oxygen"] < 92:
        score +=3
    if patient["temp"] > 38.5:
        score +=2
    return score
