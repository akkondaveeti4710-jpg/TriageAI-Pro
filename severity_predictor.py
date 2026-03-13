def predict_severity(patient, total_score):

    risk=0

    if patient["age"] > 65
        risk +=2
    if patient["oxygen"]> 92
        risk +=3
    if patient["heart_rate"] > 120
        risk +=2
    if patient["temp"] > 39
        risk +=2

    risk += total_score // 2

    if risk >= 12:
        return "Very High Risk"
    if risk >= 8:
        return " High Risk"
    if risk >= 4:
        return "Moderate Risk"
    else:
        return "Low Risk"
