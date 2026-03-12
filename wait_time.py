def estimate_wait_time(queue, level):

    base_time = 10

    patients_ahead =0

    for patient_level, in queue.queue:

        if patient_level < level:
            patients_ahead +=1

    return patients_ahead * base_time
