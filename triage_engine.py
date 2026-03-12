from triage.vital_analyzer import analyze_vitals
from risk_models.cardiac_model import cardiac_risk
from risk_models.stroke_model import stroke_risk
from risk_models.infection_model import infection_risk

def run_triage(patient):

    vitals_score = analyze_vitals(patient)

    cardiac_score = cardiac_risk(patient)

    stroke_score = stroke_risk(patient)

    infection_score = infection_risk(patient)

    total = vitals_score + cardiac_score + stroke_score + infection_score

    if total >=12:
        level = 1
    elif total >=9:
        level = 2
    elif total >= 6:
        level = 3
    elif total >= 3:
        level = 4
    else:
        level = 5

    report = f""""
Patient : {patient['name']}
Age : {patient["age"]}

Vitals Score : {vitals_score}
Cardiac Risk : {cardiac_score}
Stroke Risk : {stroke_score}
Infection Risk : {infection_score}

Total Risk Score: {total}

Assigned TRIAGE LEVEL {level}
"""""

    return level, report

def critical_alerts(patient):

    alerts = []

    if patient["oxygen"] < 88:
        alerts.append("CRITICAL: Oxygen dangerously low")
    if patient["bp_sys"] < 80:
        alerts.append("CRITICAL: Severe hypotension")
    if patient["heart_rate"] > 140:
        alerts.append("CRITICAL: Extreme tachycardia")
    return alerts
