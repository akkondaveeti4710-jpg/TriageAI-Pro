class ERPriorityQueue:

    def __init__(self):

        self.queue=[]

    def add_patient(self, patient, level):

        self.queue.append((level, patient))

        self.queue.sort(key=lambda x: x[0])

    def display_queue(self):

        print("\n=====Emergency Queue=====")

        if not self.queue:
            print("No patients in queue.")
            return

        for position, (level, patient) in enumerate(self.queue, start=1):

            print(f"{position}. level{level} - {patient['name']}")
