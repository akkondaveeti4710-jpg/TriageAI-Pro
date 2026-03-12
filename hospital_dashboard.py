class HospitalDashboard

    def __init__(self):

        self.total_patients =0

        self.level_counts = {

            1:0,
            2:0,
            3:0,
            4:0,
            5:0

        }

    def record(self, level):

        self.total_patients +=1

        if level in self.level_counts:
            self.level_counts[level] +=1

    def display_stats(self):

        print("\n======HOSPITAL ANALYTICS======")

        print("Total Patients:", self.total_patients)

        print("\nTriage Level Distribution:")

        for level, count in self.level_counts.items():

            print("Level", level, ":", count)
