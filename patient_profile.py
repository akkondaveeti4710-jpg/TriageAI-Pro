from utils. input_helpers import ask_int, ask_float, ask_yes_no

def create_patient():

    print("\n----Patient Intake---")

    name = input("Patient Name: ")

    age = ask_int("Age: ")

    heart_rate = ask_int("Heart Rate (bpm): ")

    bp_sys = ask_int("Systolic BP: ")

    bp_dia = ask_int("Diastolic BP: ")

    temperature = ask_float("Temperature (C): ")

    oxygen = ask_int("Oxygen Saturation (%): ")

    symptoms = {

        "chest_pain": ask_yes_no("Chest Pain"),
        "shortness_breath": ask_yes_no("Shortness of Breath"),
        "confusion": ask_yes_no("Confusion"),
        "severe_headache": ask_yes_no("Severe Headache"),
        "fever": ask_yes_no("Fever"),
        "dizziness":ask_yes_no("Dizziness"),
        "vomiting": ask_yes_no("Vomiting"),
        "bleeding" : ask_yes_no("Heavy Bleeding")
    }

    patient = {

        "name": name,
        "age": age,
        "heart_rate": heart_rate,
        "bp_sys": bp_sys,
        "bp_dia": bp_dia,
        "temp": temperature,
        "oxygen": oxygen,
        "symptoms": symptoms

    }

    return patient
