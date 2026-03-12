from menu import show_menu
from patient.patient_profile import create_patient
from triage.triage_engine import run_triage
from queue_system._er_priority_queue import ERPriorityQueue
from queue_system.wait_time import estimate_wait_time
from analytics.hospital_dashboard import HospitalDashboard


def main():

    queue = ERPriorityQueue()
    stats = HospitalDashboard()

    while True:

        print("\n")

        choice = show_menu()

        if choice == "1":

            patient = create_patient()

            level, report = run_triage (patient)

            queue.add_patient(patient, level)

            wait = estimate_wait_time(queue, level)

            stats. record(level)

            print("\n=========Triage Report========")
            print(report)
            print("Estimate Wait Time:", wait, "minutes")

        elif choice == "2":

            queue.display_queue()

        elif choice == "3":
            stats.display_stats()

        elif choice == "4":

            print("CLosing TriageAI Pro")
            break

        else:
            print("Invalid selection")


if __name__ == "__main__":
    main()
